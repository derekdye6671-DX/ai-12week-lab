# AI 12 周学习实验室｜两方共享资料库

这不是聊天记录备份，而是 Claude 和 OpenAI 桌面版（ChatGPT + Codex）共同参照的**项目事实记录**。

## 第一原则（用户已确认）

**把「学多少技术」让位于「你能否独立用起来」。** 凡是要敲命令的步骤由 Claude Code 执行，学习者看懂并批准；每件作品按 `PLAN.md` 里的 5 个问题验收。

## 先读哪些文件

1. `PLAN.md`：12 周计划文字版（规则、6 件作品、技能清单、逐周任务、拓展任务池）。由 Claude 维护。
2. `PROJECT_BRIEF.md`：项目目标、学习方式和分工。
3. `WEEKLY_STATUS.md`：本周目标、已验收事项和卡点。
4. `DECISIONS.md`：用户已确认的重要决定，不允许 AI 擅自修改。
5. `HANDOFF.md`：两方之间需要移交的建议、问题和结果。
6. `CLAUDE.md`：Claude Code 的协作规则。
7. `AGENTS.md`：Codex（OpenAI 桌面版）的协作规则。

## 两方分工

| 一方 | 负责 | 能写什么 |
| --- | --- | --- |
| 用户（小玄子） | 最终决策 | 全部；只有用户能批准写入 DECISIONS.md 的内容 |
| Claude（项目负责人） | 维护进度和重要决定、主开发、技术验收、合并建议 | main 分支上的全部文件 |
| OpenAI 桌面版 · Codex | 独立审查、测试、明确的小任务 | 只在 `codex/任务名` 分支上改，通过 Pull Request 交给 Claude |
| OpenAI 桌面版 · ChatGPT | 学习教练、独立顾问 | 只读；建议按 HANDOFF.md 模板写好，交给 Codex 写进分支或由用户转给 Claude |

## 两套记录的分工

- 打卡、验收、金币：以「十二周冒险岛」（Claude 维护的网页）为准。
- 计划、决定、交接：以本仓库为准。`WEEKLY_STATUS.md` 由 Claude 根据冒险岛里的验收结果填写。
- 写着「已验收」的事项，表示 Claude 已在冒险岛里确认过。

## 工作流程

- **每次开始**：在 GitHub Desktop 里点 Fetch origin，有更新就 Pull origin；然后读 `PLAN.md`、`WEEKLY_STATUS.md`、`DECISIONS.md` 和 `HANDOFF.md` 最上面的条目。
- **每次结束**：做事的一方交出成果和改动说明；Claude 核实后更新 `WEEKLY_STATUS.md` 和 `HANDOFF.md`，提交并推送。
- **一次只让一方改文件。** Claude Code 和 Codex 打开的是同一个本地文件夹 `D:\GitHub\ai-12week-lab`，两边同时改，后保存的会覆盖先保存的。
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
