# 12 周学习计划（文字版）

> 版本 2026-11-12.4｜2026-11-09 至 2027-01-31｜由 Claude 维护。
> 打卡、验收、金币以「十二周冒险岛」为准；本文件是给 Codex 和 ChatGPT 读的文字版。改动请走 HANDOFF.md，不要直接改本文件。

## 基本规则

- 学习者没有编程背景。代码和脚本由 Claude Code 写，学习者负责下指令、审查、运行和验收；亲手写代码只在可选的拓展任务里。
- **铁律（适用于以后每一个 12 周计划）**：所有涉及 GitHub 的操作，一律先给 GitHub Desktop 的点按钮做法；Desktop 做不到的（如 Pages、Issues、Actions、Release、仓库设置）才用网页，不要求学习者敲 Git 命令。任何 AI 给出 GitHub 操作步骤时都必须遵守。
- 技术类任务只有 Claude 验收后才算完成。
- 本周 Claude Code 关和 GitHub 关都验收后，可以从拓展任务池按顺序领下一个任务。
- 第 4、8、12 周是 Boss 周；第 7、8 周跨圣诞和元旦，视频可停，技术关不取消。

### 每日 5 项

- **晨练：波比 + 力量**：100 个简易波比 + 一组自重力量（俯卧撑 15、深蹲 20、平板支撑 45 秒、弓步每条腿 10），两项都做完；酸痛日可用 ≥1 小时健步走代替力量
- **12000 步**：以手机或手环为准，满 12000 才算
- **控制饮食**：按自己的饮食计划执行并记下
- **ChatGPT 英语**：固定流程：让 ChatGPT 扮演本周场景里的对方，英文对话 10 轮 → 让它列出你的 3 个错误 → 你把这 3 句改对后重说一遍；每周至少 5 天
- **主技术块**：按下面「今天的任务」做，通勤学 + 回家动手 45–60 分钟，把证明发给 Claude

## 6 件作品

| 作品 | 技术 | 完成周 | 过关标准 |
| --- | --- | --- | --- |
| 批量改名工具 | PowerShell、Claude Code | 4 | 有预览、日志、一键回滚，重名不覆盖、误选目录拒绝执行，在真实素材文件夹上跑通 |
| 自动数据报告 | Python、pip、GitHub Actions | 3（做出）/ 9（自动化） | 每周日由 Actions 用示例数据自动生成带图表的报告并提交，可手动补跑 |
| 英语词卡网站 | HTML / CSS / JS、JSON、GitHub Pages | 5 | 公开网址，手机能打开并翻卡 |
| 自己的 Skill「脚本润色」 | SKILL.md、测试用例、Pull Request | 8 | 5 组测试用例（事实、原意、自然、语气、异常输入）全部符合预期，经 PR 合并 |
| 多模型工作流 | Grok + Gemini + Claude Code + GitHub | 10 | 有脚本和说明文档（含人工审核点），按说明能重复跑一遍 |
| 作品集 + 产品草稿 v1.0 | 个人主页、Pages、tag、Release | 11–12 | 主页能看到全部成果，产品草稿写明已知限制并通过隐私清查，v1.0 Release 已发布 |

## 技能清单

**Git（GitHub Desktop）**

- G01 安装 GitHub Desktop 并登录，确认提交用的名字和隐私邮箱（第 1 周）
- G02 添加本地仓库、Clone、看改动、Commit、Push、Pull（第 1–2 周）
- G03 用 History 看提交和改动、Revert Changes in Commit 撤回提交（第 2–3 周）
- G04 新建、切换、合并分支，删除本地和远程分支（第 6 周）
- G05 在网页 Releases 打版本标签（第 12 周）

**GitHub**

- H01 账号、头像、简介、两步验证、隐私邮箱（第 1 周）
- H02 README 和 Markdown、.gitignore、规范提交说明（feat / docs / fix / chore）（第 1–2 周）
- H03 用 GitHub Pages 发布网页（第 5 周）
- H04 Issues（可让 Claude Code 批量创建）、标签、里程碑、Projects 看板、用 fixes #编号 自动关闭 Issue（第 7 周）
- H05 Pull Request：发起、检查改动、合并（第 8 周）
- H06 GitHub Actions：定时工作流、读运行日志、权限、状态徽章（第 9 周）
- H07 Fork 和读懂开源项目（第 10 周）
- H08 个人主页 README、置顶仓库、Release（第 11–12 周）

**Claude Code**

- C01 在本地仓库里下指令，审查并批准它的每一步操作（第 2 周）
- C02 /init 和 CLAUDE.md，给它定规矩（第 2 周）
- C03 安装现成 Skill（先审核来源），写自定义斜杠命令（第 6 周）
- C04 自己写 Skill 并用测试用例验证（第 8 周）
- C05 读懂并取用别人开源的规则和 Skill：辨别原版仓库、先审核再安装、按自己需要改写（第 1、6–8 周）

**脚本**

- S01 Python：安装到 D 盘、pip 装库；由 Claude Code 写读 CSV、出报告和图表的脚本，你负责运行、验收、讲清每段在做什么（真实健康数据不进公开仓库）（第 3 周）
- S02 PowerShell 脚本：由 Claude Code 写，你会运行、看懂预览和日志、会回滚；知道执行策略、脚本参数、重名和误选目录保护各防什么（第 4 周）

**数据格式**

- D01 看懂并会改 CSV、JSON、YAML、Markdown（第 各周 周）

**网页基础**

- W01 说清 HTML、CSS、JavaScript 各管什么；用本地服务器和 F12 开发者工具排错（第 5 周）

**多模型分工**

- M01 ChatGPT 讲解和写文档、Gemini 看图和出图、Grok 查实时信息和挑刺，各交出能保存、能给别人看的成果（第 每周 周）
- M02 两方协作：Claude（负责人）+ OpenAI 桌面版（ChatGPT 教练、Codex 独立审查），通过私有仓库 ai-12week-lab 共享进度、决定和交接（第 1–2 起每周 周）

**工作流**

- F01 把 Claude Code + GitHub + 至少一个其他模型串成一条能重复跑的流程（第 10 周）

## 逐周任务

### 第 1 周｜建村（11/09–11/15）

- 要交出：GitHub 账号 + GitHub Desktop + 第一个云端仓库
- Claude Code 关：建项目 + 生成频道规划 Excel（已验收）。交付：已完成
- GitHub 关：注册账号、头像、简介、两步验证（已验收）。交付：已完成
- ChatGPT 交付：技能清单 → Markdown 自测表。交付：技能自测.md
- Gemini 交付：给三个概念画一张比喻图。交付：比喻插画
- Grok 交付：查新手最常踩的 5 个坑。交付：新手避坑清单.md
- 英语：录「第 1 天」同题口语，留给第 12 周对比；场景：自我介绍
- 视频：可选：熟悉剪映，剪一条 30 秒练习短片

### 第 2 周｜Claude Code 上手（11/16–11/22）

- 要交出：Claude Code 在本地仓库里改多个文件 + CLAUDE.md + 用 GitHub Desktop 提交和同步
- Claude Code 关：第一次在本地仓库指挥 Claude Code。交付：仓库里的 CLAUDE.md、四个目录、.gitignore、practice/time.csv，至少 3 次规范提交
- GitHub 关：GitHub Desktop：克隆、拉取、推送和规范提交。交付：至少 5 次规范提交，其中 2 次是你自己用 GitHub Desktop 完成的
- ChatGPT 交付：中式英语对照表（Markdown 表格）。交付：docs/chinglish.md
- Gemini 交付：给仓库做封面横幅。交付：README 顶部横幅
- Grok 交付：英文模拟面试：Git 基础。交付：问答和评分
- 英语：场景：出差点餐
- 视频：可选：记录「我第一次让 AI 改我电脑上的文件」

### 第 3 周｜脚本与数据（11/23–11/29）

- 要交出：Python 装好 + 自动出图表的数据报告 + 会看和撤回历史
- Claude Code 关：装 Python，写一个自动出图表的数据报告。交付：scripts/stats.py + docs/weekly-report.md（含图表）
- GitHub 关：读懂历史，演练一次撤回。交付：一次 revert 提交
- ChatGPT 交付：让 ChatGPT 逐行讲解 stats.py。交付：讲解记录 + 3 道题的作答
- Gemini 交付：看图读数：从截图提取数据。交付：从截图提取的 data.csv
- Grok 交付：找 3 个值得关注的 AI 学习仓库。交付：已核对的仓库清单
- 英语：场景：开会发言
- 视频：可选

### 第 4 周｜批量整理（11/30–12/06） ⚔️ Boss 周

- 要交出：带预览、日志、回滚的批量改名工具；两关都过才算打败 Boss
- Claude Code 关：BOSS：带预览、日志和回滚的批量改名脚本。交付：rename.ps1 + undo.ps1 + 日志 + 改好名的真实文件夹
- GitHub 关：BOSS：README 命名规则章节 + 脚本入库。交付：README 命名规则 + 脚本 + About 和 Topics
- ChatGPT 交付：让 ChatGPT 给脚本加中文注释。交付：带注释的 rename.ps1
- Gemini 交付：BOSS 辅助：从截图推出命名规则。交付：命名规则-v1.md
- Grok 交付：BOSS 辅助：测命名规则清不清楚。交付：判定结果 + README 修改
- 英语：场景：写英文邮件
- 视频：可选：记录「用 AI 批量整理文件」

### 第 5 周｜网页上线（12/07–12/13）

- 要交出：一个能用手机打开的网页（GitHub Pages）
- Claude Code 关：写一个英语词卡网页并理解本地服务器。交付：index.html + cards.json，本地服务器能正常运行
- GitHub 关：用 GitHub Pages 发布网页。交付：一个能用手机打开的网址
- ChatGPT 交付：生成并校验 30 张词卡 JSON。交付：cards.json（校验通过）
- Gemini 交付：给网页挑毛病。交付：前后对比截图
- Grok 交付：给网页生成配图。交付：3 张配图已上线
- 英语：场景：机场值机和过海关
- 视频：可选：「我把一个网页送上线了」

### 第 6 周｜Skill 与命令（12/14–12/20）

- 要交出：装好现成 Skill + 自定义斜杠命令 + 分支合并
- Claude Code 关：装 Skill + 写自定义斜杠命令。交付：.claude/skills/ 下的 Skill + .claude/commands/weekly.md + 笔记
- GitHub 关：分支：新建、切换、合并、删除。交付：一次分支合并
- ChatGPT 交付：description 写法对比。交付：description-写法.md
- Gemini 交付：把 Skill 画成流程图。交付：skill-拆解.md
- Grok 交付：对照两种「技能」写法。交付：技能写法对照表.md
- 英语：场景：酒店入住和投诉
- 视频：可选

### 第 7 周｜任务管理（12/21–12/27）

- 要交出：Issues 管理 + 让 Claude Code 帮你批量建 Issue
- Claude Code 关：让 Claude Code 帮你管理 Issues。交付：5 个 Issue（由 Claude Code 创建），1 个由提交自动关闭 + Issue 速查表
- GitHub 关：Labels、Milestones 和 Projects 看板。交付：带标签和里程碑的 Issues + 一个看板
- ChatGPT 交付：用访谈法写产品大纲。交付：product/大纲.md
- Gemini 交付：给产品大纲配结构图。交付：结构图 + Issue
- Grok 交付：同类产品竞品表。交付：竞品表.md
- 英语：场景：打车和问路
- 视频：节日周可停

### 第 8 周｜写出自己的 Skill（12/28–01/03） ⚔️ Boss 周

- 要交出：自己写的 Skill 经 Pull Request 合并进仓库
- Claude Code 关：BOSS：写出自己的 Skill「脚本润色」。交付：script-polish/SKILL.md + 测试结果
- GitHub 关：BOSS：用 Pull Request 合并你的 Skill。交付：一个已合并的 PR + 使用说明
- ChatGPT 交付：打磨 Skill 规则。交付：SKILL.md 的修改提交
- Gemini 交付：BOSS 辅助：给 Skill 出测试题。交付：skill-测试用例.md
- Grok 交付：BOSS 辅助：当挑刺测试员。交付：挑刺清单 + 3 条修改
- 英语：场景：电话会议
- 视频：可停

### 第 9 周｜自动化（01/04–01/10）

- 要交出：GitHub Actions 每周自动生成周报并提交
- Claude Code 关：让 Claude Code 写一个 GitHub Actions 工作流。交付：weekly.yml + 一次成功的自动运行
- GitHub 关：读懂 Actions 运行日志和权限。交付：状态徽章 + 一次失败再修复的记录
- ChatGPT 交付：解释 YAML 语法。交付：yaml-笔记.md
- Gemini 交付：让 Gemini 审 Actions 报错。交付：对比记录
- Grok 交付：AI 圈新闻英文复述。交付：新闻复述.md
- 英语：场景：商务饭局寒暄
- 视频：可选：「仓库每周自己给我写周报」

### 第 10 周｜串起工作流（01/11–01/17）

- 要交出：Claude Code + GitHub + 至少一个其他模型的可重复工作流
- Claude Code 关：串起一条可重复的工作流。交付：workflow.ps1 + 工作流说明 + 一次完整运行的存档
- GitHub 关：Fork 开源项目，读懂它的结构。交付：一个 fork + 拆解文档
- ChatGPT 交付：工作流检查表。交付：工作流检查表.md
- Gemini 交付：工作流里负责「看图」一环。交付：提示词 + 一次输出
- Grok 交付：工作流里负责「资讯输入」一环。交付：提示词 + 一次输出
- 英语：场景：带客户参观
- 视频：可选：记录这条工作流

### 第 11 周｜作品集与产品（01/18–01/24）

- 要交出：GitHub 主页作品集 + 产品草稿 v1
- Claude Code 关：把成果整理成产品草稿 v1。交付：product/ 文件夹 + 在线网页版
- GitHub 关：GitHub 个人主页作品集。交付：个人主页 README + 置顶
- ChatGPT 交付：写一章完整示例。交付：一个验证过的示例章节
- Gemini 交付：写产品说明页。交付：产品说明.md
- Grok 交付：按终章标准查漏。交付：查漏结果 + Issues
- 英语：场景：项目汇报
- 视频：可选：讲产品草稿是怎么来的

### 第 12 周｜终章（01/25–01/31） ⚔️ Boss 周

- 要交出：v1.0 Release + 12 周复盘 + 下一个 12 周
- Claude Code 关：BOSS：用 git 数据做 12 周复盘。交付：12周复盘.md + 下一个 12 周计划
- GitHub 关：BOSS：打 v1.0 标签并发布 Release。交付：v1.0 Release
- ChatGPT 交付：英文 12 周总结讲稿。交付：讲稿 + 录音
- Gemini 交付：做 12 周作品集海报。交付：作品集海报
- Grok 交付：英文 12 周总结彩排。交付：两次评分
- 英语：录「第 84 天」同题口语并用英文讲总结
- 视频：可选：「第 1 天 vs 第 84 天口语」

## 拓展任务池（按发放顺序）

| 编号 | 任务 | 方向 | 最早第几周 |
| --- | --- | --- | --- |
| E25 | Karpathy 四条规则：读懂别人写的 CLAUDE.md | Claude Code 规则 | 1 |
| E31 | 建私有仓库 ai-12week-lab，接通 OpenAI 桌面版 | AI 协作 | 1 |
| E01 | 看看 .git 文件夹里装了什么 | Git 原理 | 1 |
| E02 | 正则表达式入门：5 个实用匹配 | 正则表达式 | 1 |
| E03 | 放弃改动、比较分支、在网页上查看 | GitHub Desktop 进阶 | 1 |
| E04 | Stash：临时收起做到一半的改动 | GitHub Desktop 进阶 | 2 |
| E05 | 故意制造并解决一次合并冲突 | GitHub Desktop 进阶 | 2 |
| E06 | 后悔药：让 Claude Code 帮你救回「丢掉」的提交 | Git 原理 | 2 |
| E07 | Python 基础一：变量、条件、循环 | Python 基础 | 3 |
| E08 | Python 基础二：函数、读文件、处理错误 | Python 基础 | 3 |
| E09 | 虚拟环境 venv：每个项目的库互不干扰 | Python 基础 | 3 |
| E10 | pandas + openpyxl 自动生成 Excel | Python 进阶 | 3 |
| E11 | ffmpeg 入门：命令行处理视频 | 视频自动化 | 4 |
| E12 | 批量压缩视频脚本 | 视频自动化 | 4 |
| E13 | Whisper 自动出字幕 | 视频自动化 | 4 |
| E14 | Windows 任务计划程序：让电脑定时干活 | 本地自动化 | 4 |
| E15 | settings.json：规定 Claude Code 能做什么 | Claude Code 进阶 | 6 |
| E16 | Hooks：让检查自动发生 | Claude Code 进阶 | 6 |
| E17 | 分支保护：不许直接改主线 | GitHub 进阶 | 6 |
| E18 | MCP：给 Claude Code 接上外部工具 | Claude Code 进阶 | 7 |
| E19 | Codespaces：浏览器里的云端电脑 | GitHub 进阶 | 7 |
| E20 | 子代理：做一个专门的代码审查员 | Claude Code 进阶 | 8 |
| E21 | 用 Python 调用 Claude API | AI API | 9 |
| E22 | Actions Secrets：在自动化里安全使用密钥 | GitHub 进阶 | 9 |
| E23 | 做一个 Discord 英语词卡机器人 | AI API | 10 |
| E24 | 无界面模式：在脚本里调用 Claude Code | Claude Code 进阶 | 10 |
| E26 | 跑通 ppt-master：把 Word 变成可编辑 PPT | 开源工具 | 3 |
| E27 | diagram-design：给频道做统一风格的示意图 | 开源工具 | 5 |
| E28 | 拆解 mattpocock/skills，改出你自己的版本 | Claude Code 进阶 | 6 |
| E29 | claude-mem：让 Claude Code 记住上次做了什么 | Claude Code 进阶 | 7 |
| E30 | VoiceStudio：本地配音和转写（先测电脑能不能跑） | 视频自动化 | 8 |

## 想加内容怎么办

ChatGPT 或 Codex 想增加实用类、工具类内容时，按 HANDOFF.md 的模板写成「建议」，写清：放在第几周、替换还是新增、预计多少分钟、交付物和验收证明。用户确认后由 Claude 写进冒险岛和本文件，避免出现两份计划。
