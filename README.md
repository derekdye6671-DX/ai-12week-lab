# AI 12 周学习实验室｜三方共享资料库

这不是聊天记录备份，而是 Claude Code、Codex、ChatGPT 共同参照的**项目事实记录**。

## 先读哪些文件

1. `PROJECT_BRIEF.md`：项目目标、适合的学习方式和分工。
2. `WEEKLY_STATUS.md`：当前周目标、已经完成的事项和卡点。
3. `DECISIONS.md`：用户已确认的重要决定，不允许 AI 擅自修改。
4. `HANDOFF.md`：AI 之间需要移交的建议、问题和结果。
5. `CLAUDE.md`：Claude Code 的项目协作规则。
6. `AGENTS.md`：Codex 的项目协作规则。

## 最简单的使用流程

- 每次开始：读 `PROJECT_BRIEF.md`、`WEEKLY_STATUS.md`、`DECISIONS.md`，必要时读 `HANDOFF.md`。
- 开发工作：由 Claude Code 主开发；Codex 优先独立检查、测试、承担界限明确的小任务。
- 每次结束：由执行方提供成果与变更说明；Claude Code 核实后更新 `WEEKLY_STATUS.md` 和 `HANDOFF.md`，提交到 GitHub。
- 重大调整：先在 `HANDOFF.md` 记录建议，由用户确认后才写入 `DECISIONS.md`。
- ChatGPT：连接 GitHub 后读取资料给出评估；它通常不能通过 GitHub 连接直接写回仓库，需将建议交由 Claude Code 合并。

## 安全边界

禁止将密码、API Key、访问令牌、客户商业机密、个人隐私或不具备分享授权的资料提交到 GitHub。真实业务数据须脱敏或使用模拟数据。

## 首次建立仓库

在 GitHub 创建一个**私有**仓库（例如 `ai-12week-lab`），将本文件夹中的所有文件上传到仓库根目录。Claude Code 与 Codex 使用同一个仓库；在 ChatGPT 插件设置中单独授权它访问。

## 重要说明

- 三种 AI **不会自动共享聊天历史**；只有实际写入并推送到仓库的更新才会成为可靠共同资料。
- Codex 云端通常读取 GitHub 上的版本，电脑里没有推送的本地修改不会自动出现。
- 项目计划修改以用户确认后的 `DECISIONS.md` 为准，不能只凭某个 AI 的口头建议。
