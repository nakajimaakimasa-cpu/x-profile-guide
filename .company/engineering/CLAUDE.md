# 開発

## 役割
X API連携、自動投稿システム、トレンド検知ボット、分析ダッシュボードの設計・開発を管理する。

## ルール
- 技術ドキュメントは `docs/topic-name.md`
- デバッグログは `debug-log/YYYY-MM-DD-issue-name.md`
- デバッグのステータス: open → investigating → resolved → closed
- 設計書は必ず「概要」「設計・方針」「詳細」の構成にする
- バグ修正時は「再発防止」セクションを必ず記入
- 技術的な意思決定はCEOのdecisionsにもログを残す

## X自動投稿システムの技術スタック（候補）
- X API v2 (OAuth 2.0)
- Python (tweepy / httpx)
- スケジューラ: cron / APScheduler / Celery
- AI: GPT-5.4 API（投稿文生成）
- データ保存: SQLite / Supabase
- デプロイ: Railway / Render / VPS

## フォルダ構成
- `docs/` - 技術ドキュメント・設計書
- `debug-log/` - デバッグ・バグ調査ログ
