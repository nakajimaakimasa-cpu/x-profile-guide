---
topic: OpenClaw × Addness の掛け合わせ
date: 2026-02-22
article_type: experience-review / vision-product ハイブリッド
related_idea: なし
---

# OpenClaw × Addness に関するリサーチメモ

## 概要

OpenClawは2025年11月にオーストリア人開発者Peter Steinbergerが公開したオープンソースのAIエージェント。
GitHub史上最速で10万スターを達成（約2日間）し、2026年2月時点で216,000+スター、40,000+フォーク。
「指示したタスクを実際に実行するAI」として、単なるチャットAIではなく「手足を持ったAIアシスタント」。

## キーデータ

- GitHub Stars: 216,000+（2026年2月時点）
- フォーク数: 40,000+
- コントリビューター: 370+
- ライセンス: MIT
- 対応プラットフォーム: WhatsApp, Telegram, Slack, Discord, Teams, Signal, iMessage他13+
- ClawHub スキル数: 5,700+（うち安全確認済み3,286）
- 1週間でWebサイト200万訪問
- 対応AIモデル: Claude, GPT, Gemini, Grok, ローカルモデル(Ollama)
- Peter Steinberger: 2026年2月にOpenAIに参画
- 改名歴: Clawdbot → Moltbot → OpenClaw（Anthropicの商標問題）

## OpenClawの「Brain & Hands」アーキテクチャ

- Brain（推論エンジン）: LLMが要求を解釈し行動を決定。ファイルやネットワークに直接触れない
- Hands（実行環境）: Shell / Filesystem / Browser / HTTP の4つの実行能力
- JSONメッセージによる構造化されたツールコール通信
- Brainが行動を計画 → Handsが実行 → 結果をBrainに返す → 次の行動を判断

## 活用事例

- 全自動開発: TODO.md → Claude Code連携 → 自律型プランナー・エグゼキューターモデル
- 業務自動化: メール処理、スケジュール管理、経理、競合調査
- M&A案件管理: メール監視→スクレイピング→スプレッドシート→Slack通知（1件3分→5秒）
- 週25時間の業務が72時間で40%削減
- 毎日45分のニュース要約が3分に短縮

## コスト・課題

- API費用: 1日最大$300（ヘビー利用時）
- セキュリティ: ClawHubに386個以上の悪意あるスキル発見
- プロンプトインジェクション攻撃のリスク
- 権限管理・監査ログが必須

## ロボティクスの展開

- ClawBody: OpenClawを物理ハードウェアに接続するソフトウェアブリッジ
- MuJoCoシミュレーションで訓練→実ロボットにデプロイ
- $500以下で機能的なロボットシステム構築可能
- PicoClaw: Go言語製超軽量版。$10で動作、1秒未満で起動

## 業界の「常識」（ぶった切り候補）

- 常識1: 「AIは質問に答えるもの」→ OpenClawは「AIが実際に仕事をする」を証明した
- 常識2: 「AIエージェントはまだ研究段階」→ すでに216,000+人が実用している
- 常識3: 「AIに仕事を任せるには細かい指示が必要」→ Brain & Handsの分離で自律実行

## アドネス哲学との接続ポイント

- Well-being: AIが面倒なタスクを実行 → 人間は意義のある仕事・関係構築に集中 → Well-being向上
- LTR: AIエージェントは24/7稼働 → 顧客への継続的な価値提供 → 長期関係構築の自動化
- Giver/Taker: OpenClawで自動化した分の時間をGiveに回せる → Give Super Hard Foreverの物理的実装
- 価値提供: OpenClaw = 実行能力 / Addness = 目標→行動の変換能力 → 組み合わせ = 価値提供の自動化
- アドる: 「ググるとわかる。アドればできる。」→ OpenClawによって「できる」が文字通り自動化
  - Addnessが目標を分解 → OpenClawが実行 = 「アドる」の完成形

## 核心の接続ロジック

OpenClawの最大の弱点 = 「何を実行させるか」は人間が考えなければならない
→ Addnessの「AI Goal Breakdown」が目標→行動を自動分解
→ OpenClawの「Brain & Hands」がその行動を自動実行
→ 人間は「目標を決める」だけでいい
→ これこそ「アドる」の最終形態

Brain & Hands アーキテクチャは、まさにAddnessの思想と同じ構造:
- Brain = 思考（目標を理解し、何をすべきか決める）= Addnessの「ゴール分解」
- Hands = 実行（決まったことを実際にやる）= 「できる」の民主化

## みかみの体験談で使えそうなもの

- 東大中退→起業の「知ってるのにできない」体験
- 留置所での覚醒（力なきギバーは偽善）→ AIに力を持たせる
- 未経験300人の組織運営 → 全員にAIエージェントがつく未来
- 100万円とダンボール机での創業 → 今は月商5億 → 次のジャンプはAIエージェント

## 記事の切り口候補

1. 体験レビュー × ビジョン: OpenClawとAddnessを実際に組み合わせてみた衝撃
2. 等式変換: OpenClaw = AIの「手足」、Addness = AIの「目標」→ 合体 = AIの「人生」
3. 「アドる」の完成形: テクノロジーが哲学に追いついた瞬間

## 参考リンク

- https://github.com/openclaw/openclaw
- https://openclaw.ai/
- https://clawdocs.org/architecture/brain-and-hands/
- https://www.openclawrobotics.com/
- https://claw-hub.net/
- https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai
