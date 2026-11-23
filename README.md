# AI 12 周学习实验室｜多方共享资料库

这不是聊天记录备份，而是 Claude、ChatGPT / Codex、Gemini、Grok 共同参照的**项目事实记录**。每个 12 周计划的相关信息都放在本仓库；计划产出的成品和作业放在 xiaoxuanzi-channel。

## 第一原则（用户已确认）

**把「学多少技术」让位于「你能否独立用起来」。** 凡是要敲命令的步骤由 Claude Code 执行，学习者看懂并批准；每件作品按 `PLAN.md` 里的 5 个问题验收。

## 先读哪些文件

0. **`docs/36周总计划与第1个12周细分计划.md`：36 周总计划与第 1 个 12 周细分计划（当前主文件，和其他文件冲突时以它为准）。**
1. `PLAN.md`：12 周计划文字版（规则、6 件作品、技能清单、逐周任务、拓展任务池）。由 Claude 维护。
2. `PROJECT_BRIEF.md`：项目目标、学习方式和分工。
3. `WEEKLY_STATUS.md`：本周目标、已验收事项和卡点。
4. `DECISIONS.md`：用户已确认的重要决定，不允许 AI 擅自修改。
5. `HANDOFF.md`：各方之间需要移交的建议、问题和结果（只有 Claude 写入，其他 AI 的建议放 `docs/建议/`）。
6. `CLAUDE.md`：Claude Code 的协作规则。
7. `AGENTS.md`：Codex（OpenAI 桌面版）的协作规则。

## 三级权限（2026-11-23 用户定为铁律）

| 级别 | AI | 能写什么 |
| --- | --- | --- |
| 用户（小玄子） | 最终决策者 | 全部；只有用户能批准写入 DECISIONS.md 的内容 |
| 一级 | Claude、Claude Code（唯一汇总协调人） | 用户批准后改 main 上的核心文件；审核并合并别人的 PR |
| 二级 | ChatGPT、Codex（归在 ChatGPT 名下） | 在 `chatgpt/…`、`codex/…` 分支上新增建议文件或提议修改，发 PR 由 Claude 审核；不直接改 main |
| 三级 | Gemini、Grok（含 Grok Bot） | 只新增 `docs/建议/<名字>/`、`docs/调研/` 下的文件；不改任何已有文件 |

Perplexity 11/23 起暂停（额度用完），恢复后作为三级调研备选。分支名一律用英文。

## 两套记录的分工

- 打卡、验收、金币：以冒险岛网页（公开仓库 quest-island 的 verified.json）为准。
- 计划、决定、交接：以本仓库为准。`WEEKLY_STATUS.md` 由 Claude 根据冒险岛里的验收结果填写。
- 写着「已验收」的事项，表示 Claude 已在冒险岛里确认过。

## 工作流程

- **每次开始**：在 GitHub Desktop 里点 Fetch origin，有更新就 Pull origin；然后读 `PLAN.md`、`WEEKLY_STATUS.md`、`DECISIONS.md` 和 `HANDOFF.md` 最上面的条目。
- **每次结束**：做事的一方交出成果和改动说明；Claude 核实后更新 `WEEKLY_STATUS.md` 和 `HANDOFF.md`，提交并推送。
- **一次只让一个 AI 改同一个文件。** Claude Code 和 Codex 打开的是同一个本地文件夹 `D:\GitHub\ai-12week-lab`，两边同时改，后保存的会覆盖先保存的。
- **重大调整**：先在 `HANDOFF.md` 记录建议，用户确认后才写入 `DECISIONS.md` 和 `PLAN.md`。

## 铁律：GitHub 操作优先用 GitHub Desktop

给用户的所有 GitHub 操作步骤，一律先给 GitHub Desktop 的点按钮做法；Desktop 做不到的（如 Pages、Issues、Actions、Release、仓库和权限设置）才用网页。不要让用户敲 Git 命令。适用于以后每一个 12 周计划。

## 放哪个仓库

- 作品、脚本、网页：`xiaoxuanzi-channel`（公开）。
- 计划、进度、交接：本仓库 `ai-12week-lab`（私有）。不要为了发布作品而公开本仓库。

## 安全边界

禁止将密码、API Key、访问令牌、客户商业机密、真实健康数据、个人隐私或不具备分享授权的资料提交到 GitHub，私有仓库也一样。真实业务数据须脱敏或使用模拟数据。

## 仓库信息

- 私有仓库 `derekdye6671-DX/ai-12week-lab`，本地位置 `D:\GitHub\ai-12week-lab`，2026-11-12 建立。
- 原始资料包保留在 `D:\AI_12周三方同步资料包`，作为备份，不再修改。
- ChatGPT 聊天和 Codex 虽在同一个应用里，是否自动共享内容尚未验证；在验证前，OpenAI 一方以 Codex 打开的仓库文件为准。
