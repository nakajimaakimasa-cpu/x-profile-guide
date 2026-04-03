from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from x_ops_common import (  # noqa: E402
    REPLIES_DIR,
    REPLIES_INBOX_DIR,
    datetime_to_unix_seconds,
    ensure_runtime_dirs,
    format_reply_item,
    iso_now,
    load_environment,
    now_local,
    parse_twitter_datetime,
    read_state,
    send_telegram_message,
    timestamp_slug,
    twitterapi_get,
    write_json,
    write_state,
    write_text,
)


STATE_NAME = "mentions_state"
MAX_SEEN_IDS = 200


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TwitterAPI.ioで新着メンションを取得します。")
    parser.add_argument("--user-name", default="", help="取得対象のXユーザー名。未指定時は X_USERNAME を使用します。")
    parser.add_argument("--notify", action="store_true", help="新着があった場合にTelegram通知を送ります。")
    return parser.parse_args()


def resolve_username(explicit_username: str) -> str:
    username = explicit_username or os.getenv("X_USERNAME", "").strip()
    if not username:
        raise RuntimeError("X_USERNAME が設定されていません。")
    return username.lstrip("@")


def fetch_new_mentions(user_name: str) -> tuple[list[dict], dict]:
    state = read_state(STATE_NAME, default={"last_checked_at": 0, "seen_tweet_ids": []})
    seen_ids = list(state.get("seen_tweet_ids", []))
    last_checked = int(state.get("last_checked_at", 0))
    # 初回起動時（状態なし）は現在時刻をセットし、過去の返信を取得しない
    if last_checked == 0:
        init_time = int(now_local().timestamp())
        return [], {"last_checked_at": init_time, "seen_tweet_ids": []}
    since_time = max(last_checked - 120, 0)
    response = twitterapi_get("/twitter/user/mentions", {"userName": user_name, "sinceTime": since_time, "cursor": ""})
    tweets = response.get("tweets", []) if isinstance(response, dict) else []
    fresh_mentions: list[dict] = []
    latest_seen_at = int(state.get("last_checked_at", 0))
    for tweet in tweets:
        tweet_id = str(tweet.get("id", ""))
        if not tweet_id or tweet_id in seen_ids:
            continue
        author_name = str((tweet.get("author") or {}).get("userName", "")).lower()
        if author_name == user_name.lower():
            continue
        created_at = tweet.get("createdAt", "")
        try:
            created_ts = datetime_to_unix_seconds(parse_twitter_datetime(created_at))
        except Exception:
            created_ts = int(now_local().timestamp())
        latest_seen_at = max(latest_seen_at, created_ts)
        tweet["createdAtUnix"] = created_ts
        fresh_mentions.append(tweet)
    updated_state = {
        "last_checked_at": latest_seen_at or int(now_local().timestamp()),
        "seen_tweet_ids": (seen_ids + [str(tweet.get("id", "")) for tweet in fresh_mentions])[-MAX_SEEN_IDS:],
    }
    return fresh_mentions, updated_state


def save_mentions_output(mentions: list[dict], user_name: str) -> tuple[Path, Path]:
    stamp = timestamp_slug()
    json_path = REPLIES_INBOX_DIR / f"{stamp}-mentions.json"
    md_path = REPLIES_DIR / "pending.md"
    payload = {"generated_at": iso_now(), "user_name": user_name, "count": len(mentions), "mentions": mentions}
    write_json(json_path, payload)
    sections = [
        "# 未処理リプ一覧",
        "",
        f"- generated_at: {payload['generated_at']}",
        f"- target_user: @{user_name}",
        f"- count: {len(mentions)}",
        "",
    ]
    if mentions:
        for index, tweet in enumerate(mentions, start=1):
            sections.append(format_reply_item(tweet, index))
    else:
        sections.extend(["新着リプはありません。", ""])
    write_text(md_path, "\n".join(sections))
    return json_path, md_path


def main() -> int:
    args = parse_args()
    load_environment()
    ensure_runtime_dirs()
    user_name = resolve_username(args.user_name)
    mentions, updated_state = fetch_new_mentions(user_name)
    json_path, md_path = save_mentions_output(mentions, user_name)
    write_state(STATE_NAME, updated_state)
    print(f"対象ユーザー: @{user_name}")
    print(f"新着件数: {len(mentions)}")
    print(f"JSON保存: {json_path}")
    print(f"Markdown保存: {md_path}")
    if args.notify and mentions:
        send_telegram_message(f"Xメンション検知: @{user_name} に {len(mentions)} 件の新着リプがあります。")
        print("Telegram通知を試行しました。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
