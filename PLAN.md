# 12 周学习计划（文字版）

> 版本 2026-11-12.5｜2026-11-09 至 2027-01-31｜由 Claude 维护。
> 打卡、验收、金币以「十二周冒险岛」为准；本文件是给 Codex 和 ChatGPT 读的文字版。改动请走 HANDOFF.md，不要直接改本文件。

## 第一原则（用户已确认）

**把「学多少技术」让位于「你能否独立用起来」。**

学习者没有任何编程背景。允许借助 AI 和操作说明，但要能：启动工具、准备输入、判断输出是否合理、出错时停下并恢复。凡是要敲命令的步骤，一律由 Claude Code 执行，学习者看懂用途再批准；不以记住命令或逐行解释代码为目标。

每件作品验收都问 5 个问题：

1. 它解决了我的什么实际问题？
2. 我知道从哪里启动、需要准备什么输入吗？
3. 我能判断结果对不对，知道哪些还需要人工核查吗？
4. 出错时，我知道怎样停下、保护原件、恢复或求助吗？
5. 换一份同类示例数据，照着说明我还能再做一次吗？

## 基本规则

- **铁律（适用于以后每一个 12 周计划）**：所有涉及 GitHub 的操作，一律先给 GitHub Desktop 的点按钮做法；Desktop 做不到的（如 Pages、Issues、Actions、Release、仓库设置）才用网页，不要求学习者敲 Git 命令。任何 AI 给出 GitHub 操作步骤时都必须遵守。
- **放哪个仓库**：作品、脚本、网页放 xiaoxuanzi-channel（公开）；计划、进度、交接放 ai-12week-lab（私有）。下面任务里没有特别说明的「仓库」都指 xiaoxuanzi-channel。不要为了发布作品而公开 ai-12week-lab。
- **数据安全**：真实健康数据、工作资料、客户信息和个人隐私不进任何仓库（私有仓库也不行），练习一律用模拟数据。密钥不得出现在代码、截图、日志或提交历史里。
- **ChatGPT 的角色**：只出建议和文本，不直接改文件；由 Claude Code 落盘，学习者用 GitHub Desktop 提交。
- **Codex 只读检查**：网页公开前、自动化获得写权限前、脚本碰真实文件前，先让 Codex 只读检查一遍。
- 技术类任务只有 Claude 验收后才算完成。
- **拓展任务**：本周 Claude Code 关和 GitHub 关都验收后才能领；按下表顺序，领第一个「最早第几周」已到的任务；做完验收后可以再领。
- 第 4、8、12 周是 Boss 周；第 7、8 周跨圣诞和元旦，视频可停，技术关不取消。

### 每日 5 项

- **晨练：波比 + 力量**：100 个简易波比 + 一组自重力量（俯卧撑 15、深蹲 20、平板支撑 45 秒、弓步每条腿 10），两项都做完；酸痛日可用 ≥1 小时健步走代替力量
- **12000 步**：以手机或手环为准，满 12000 才算
- **控制饮食**：按自己的饮食计划执行并记下
- **ChatGPT 英语**：固定流程：让 ChatGPT 扮演本周场景里的对方，英文对话 10 轮 → 让它列出你的 3 个错误 → 你把这 3 句改对后重说一遍；每周至少 5 天
- **主技术块**：按下面「今天的任务」做，通勤学 + 回家动手 45–60 分钟，把证明发给 Claude

「主技术块」每天做什么，见下面每周的「每日安排」。

## 6 件作品

| 作品 | 技术 | 完成周 | 过关标准 |
| --- | --- | --- | --- |
| 一键 PPT 汇报 | Claude Code 写 Python（python-pptx）、Excel、PowerPoint | 4 | 双击一个入口就能从 CSV 生成 Excel 和可编辑的 PPT；数字与原表一致；换一份数据，只看说明能自己再做一次 |
| Excel 自动报表 | Claude Code 写 Python（openpyxl）、GitHub Actions | 3（做出）/ 9（自动化） | 含公式、格式和图表，能手动核对关键数字；每周日由 Actions 用模拟数据自动生成并提交，可手动补跑 |
| 英语词卡网站 | HTML / CSS / JS、JSON、GitHub Pages | 5 | 公开前经 Codex 只读检查，公开网址，手机能打开并翻卡 |
| 自己的 Skill「脚本润色」 | SKILL.md、测试用例、Pull Request | 8 | 5 组测试用例（事实、原意、自然、语气、异常输入）全部符合预期，经 PR 合并 |
| 多模型工作流 | Grok + Gemini + Claude Code + GitHub | 10 | 有脚本和说明文档（含人工审核点），按说明能重复跑一遍 |
| 作品集 + 产品草稿 v1.0 | 个人主页、Pages、tag、Release | 11–12 | 主页能看到全部成果，产品草稿写明已知限制并通过隐私清查，v1.0 Release 已发布 |

每件作品另外都要通过上面的 5 个验收问题。

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

**办公自动化（脚本由 Claude Code 写）**

- S01 Excel 自动报表：由 Claude Code 配好 Python 环境（D 盘、.venv）并写脚本；你会放入数据、运行、核对关键数字、出错时用副本恢复（只用模拟数据）（第 3 周）
- S02 一键 PPT：从 Excel 生成可编辑的 PPT、换模板、双击入口运行；能判断数字和图表对不对（第 4 周）

**数据格式**

- D01 看懂并会改 CSV、JSON、YAML、Markdown（第 各周 周）

**网页基础**

- W01 说清 HTML、CSS、JavaScript 各管什么；让 Claude Code 启动本地预览，用 F12 开发者工具看报错（第 5 周）

**多模型分工**

- M01 ChatGPT 讲解和写文档、Gemini 看图和出图、Grok 查实时信息和挑刺，各交出能保存、能给别人看的成果（第 每周 周）
- M02 两方协作：Claude（负责人）+ OpenAI 桌面版（ChatGPT 教练、Codex 独立审查），通过私有仓库 ai-12week-lab 共享进度、决定和交接（第 1–2 起每周 周）

**工作流**

- F01 把 Claude Code + GitHub + 至少一个其他模型串成一条能重复跑的流程（第 10 周）

## 逐周任务

### 第 1 周｜建村（11/09–11/15）

要交出：GitHub 账号 + GitHub Desktop + 第一个云端仓库

**Claude Code 关：建项目 + 生成频道规划 Excel（已验收）**

1. 11/09 已完成

- 交付：已完成
- 验收证明：已验收

**GitHub 关：注册账号、头像、简介、两步验证（已验收）**

1. 11/11 已完成

- 交付：已完成
- 验收证明：已验收

**模型交付**

- ChatGPT：技能清单 → Markdown 自测表。把「十二周技能与作品清单（确认版）」第一部分的技能清单发给 ChatGPT；让它整理成 Markdown 任务列表（每行 - [ ] 开头），每项后面配一道自测题；存成 技能自测.md，第 2 周放进仓库，每学会一项就把 [ ] 改成 [x]。交付：技能自测.md
- Gemini：给三个概念画一张比喻图。确认 Gemini 能正常登录；告诉它你对仓库、提交、推送的理解，让它想一个生活化比喻；让它生成一张横版插画，带三个中文标注，改到满意后下载。交付：比喻插画
- Grok：查新手最常踩的 5 个坑。确认 Grok 能正常登录；让它搜最近一个月 X 上关于 GitHub 或 Claude Code 新手的讨论；总结 5 个常踩的坑，每条附原帖链接；你挑 2 条写怎么避免，存成文件。交付：新手避坑清单.md

**每日安排（主技术块）**

- 周一：建项目 + 生成 Excel——已完成
- 周二：注册 GitHub、头像简介、两步验证——已完成
- 周三：装 GitHub App + 讲清三个概念——已完成
- 周四：今晚：装 GitHub Desktop，建云端仓库并第一次推送——（11/12 起 Git 操作改用 GitHub Desktop）① 从 desktop.github.com 下载安装 GitHub Desktop，File → Options → Accounts 登录 GitHub，Options → Git 确认名字和邮箱 ② 在 D 盘新建文件夹 GitHub ③ GitHub 网页右上角 + → New repository：名字 xiaoxuanzi-channel，选 Public，勾 Add a README，Create ④ GitHub Desktop 里 File → Clone repository，选 xiaoxuanzi-channel，Local path 选 D:\GitHub，点 Clone ⑤ 用记事本打开 D:\GitHub\xiaoxuanzi-channel\README.md，加三行自我介绍并保存 ⑥ 回 GitHub Desktop，左侧 Changes 能看到红绿改动，Summary 写「docs: 添加自我介绍」，点 Commit to main，再点 Push origin ⑦ 点 History 看到 2 条提交，刷新网页确认 README 已更新（验收证明：仓库链接 + GitHub Desktop 的 History 截图）
- 周五：GitHub Desktop 初体验——File → Add local repository，选已经建好的 D:\git-test；用记事本在里面新建 a.txt 写一句话 → 回 GitHub Desktop 看左侧 Changes → Summary 写 first → 点 Commit to master → 改 a.txt，看红绿改动 → 再提交一次 → 点 History 看到 2 条（验收证明：GitHub Desktop 的 History 截图，能看到 2 次提交）
- 周六：看懂真实仓库 + 把答案提交进自己的仓库——打开 github.com/anthropics/skills，回答：README 在哪、多少次提交、几个分支、多少 Star、最近一次提交是什么时候；把五个答案写成 xiaoxuanzi-channel 里的 docs/读仓库练习.md，在 GitHub Desktop 里 Commit（Summary 用 docs: 开头）→ Push origin（验收证明：文件的仓库链接）
- 周日：ChatGPT 技能自测表 + Gemini 比喻图 + 周复盘——按本周 ChatGPT、Gemini 交付做；把技能自测.md 提交进仓库；写周复盘（验收证明：仓库里技能自测.md 链接）

- 英语：录「第 1 天」同题口语，留给第 12 周对比；场景：自我介绍
- 视频：可选：熟悉剪映，剪一条 30 秒练习短片

### 第 2 周｜Claude Code 上手（11/16–11/22）

要交出：Claude Code 在本地仓库里改多个文件 + CLAUDE.md + 用 GitHub Desktop 提交和同步

**Claude Code 关：第一次在本地仓库指挥 Claude Code**

1. 在桌面版里开一个 Claude Code 会话，选中本地文件夹 D:\GitHub\xiaoxuanzi-channel
2. 指令：「读这个仓库，用三句话告诉我它现在有什么」，看它执行了哪些读取操作
3. 输入 /init，让它生成 CLAUDE.md，逐段读懂
4. 在 CLAUDE.md 补 5 条规则：项目用途、目录结构、提交说明格式（feat/docs/fix/chore）、禁止提交视频素材、禁止提交密钥和个人隐私数据
5. 指令：「按 CLAUDE.md 建 docs、scripts、assets、practice 四个目录，各放 .gitkeep，并写 .gitignore 忽略 *.mp4 *.mov 素材/」
6. 把频道规划 Excel 复制到 practice/，指令：「把『每周时间分配』工作表导出成 time.csv」，用记事本打开看懂 CSV
7. 每次它要改文件时，看清楚改动再批准；最后让它用规范的提交说明提交

- 交付：仓库里的 CLAUDE.md、四个目录、.gitignore、practice/time.csv，至少 3 次规范提交（计入本周 GitHub 关要求的 5 次）
- 验收证明：仓库链接

**GitHub 关：GitHub Desktop：克隆、拉取、推送和规范提交**

1. （第 1 周已克隆过可跳过）GitHub Desktop 里 File → Clone repository，选 xiaoxuanzi-channel，Local path 选 D:\GitHub，理解 clone 是把云端仓库完整复制到本地
2. 在网页上改一次 README，回 GitHub Desktop 点 Fetch origin，再点 Pull origin 拉下来
3. 本地改文件后，在左侧 Changes 看红绿改动，Summary 写「docs: …」，点 Commit to main，再点 Push origin
4. 点左侧 History 看提交历史
5. Claude Code 的提交也会出现在 History 里，对照看它写的提交说明

- 交付：至少 5 次规范提交，其中 2 次是你自己用 GitHub Desktop 完成的
- 验收证明：Commits 页面截图

**模型交付**

- ChatGPT：中式英语对照表（Markdown 表格）。列出你常犯的 10 个中式英语说法；让 ChatGPT 输出 Markdown 表格：中式说法 | 地道说法 | 例句；交给 Claude Code 存成 docs/chinglish.md，你在 GitHub Desktop 里提交，再到网页上看表格效果。交付：docs/chinglish.md
- Gemini：给仓库做封面横幅。告诉 Gemini 仓库用途：普通打工人用 AI 学技术的记录；生成 1280×640 横幅，写上 xiaoxuanzi-channel；存成 assets/banner.png，README 第一行写 ![](assets/banner.png)。交付：README 顶部横幅
- Grok：英文模拟面试：Git 基础。让 Grok 当严格的面试官，用英文问你 5 个关于 clone、commit、push、pull 的问题；你用英文回答；让它逐题打分、纠正英文和概念错误。交付：问答和评分

**每日安排（主技术块）**

- 周一：第一次在本地仓库指挥 Claude Code——在桌面版 Claude Code 里选中 D:\GitHub\xiaoxuanzi-channel，让它读仓库并总结；观察它执行的每个操作，学会看懂并批准（验收证明：对话截图）
- 周二：/init 生成 CLAUDE.md 并补规则——输入 /init，读懂生成的内容；补 4 条规则（用途、目录、提交格式、禁传视频）；做过 E25 的话，再把 Karpathy 四条规则用你的中文版合并进去；让它按规则建四个目录和 .gitignore（验收证明：仓库目录截图）
- 周三：Excel 导出 CSV——把规划表复制到 practice/，让 Claude Code 导出 time.csv；用记事本打开理解 CSV 格式；让它用 feat: 提交（验收证明：time.csv 链接）
- 周四：拉取和规范提交——在网页上改一次 README，GitHub Desktop 点 Fetch origin 再 Pull origin 拉下来；自己完成 2 次提交，Summary 分别用 docs: 和 chore: 开头（验收证明：Commits 截图）
- 周五：用 History 读历史——在 GitHub Desktop 的 History 里逐条点开提交，看每次改了哪些文件；对照网页 Commits 页面，分清哪些是你提交的、哪些是 Claude Code 提交的（验收证明：一句话说明 History 里一条提交能看到哪些信息）
- 周六：Gemini 横幅 + README 美化——按本周 Gemini 交付生成横幅；README 用标题、列表、图片、链接重写（验收证明：仓库首页截图）
- 周日：中式英语表 + Grok 英文面试 + 周复盘——按本周 ChatGPT、Grok 交付做；写周复盘（验收证明：文件链接）

- 英语：场景：出差点餐
- 视频：可选：记录「我第一次让 AI 改我电脑上的文件」

### 第 3 周｜Excel 自动报表（11/23–11/29）

要交出：Claude Code 做的 Excel 自动周报（公式、格式、图表）+ 会看和撤回历史

**Claude Code 关：让 Claude Code 做一份 Excel 自动周报**

1. 在 Claude Code 里打开 D:\GitHub\xiaoxuanzi-channel，对它说：「帮我准备好 Python 运行环境：装到 D:\Python，在仓库里建 .venv 虚拟环境，装好 openpyxl，并把 .venv 加进 .gitignore」。它运行的每条命令，看懂用途再批准
2. 让它生成模拟的频道运营数据 practice/sample-data.csv（日期、视频标题、平台、播放量、点赞、涨粉，4 周约 20 行），不用任何真实个人数据
3. 让它写 scripts/make_report.py：读 sample-data.csv，生成 reports/周报.xlsx，含每周播放、点赞、涨粉合计（用 Excel 公式算）、播放量前 3 名标绿、一张每周播放量折线图
4. 让它运行一次，你用 Excel 打开周报，手动核对 3 个数字：第 1 周总播放、播放最高的视频、总涨粉，和 CSV 对得上
5. 换数据再做一次：让它复制出 sample-data-2.csv 并改几行数字，再生成一次，确认报表跟着变；原始 CSV 永远不改
6. 让它写 reports/README.md：从哪启动、准备什么输入、怎么判断结果对、出错怎么办

- 交付：scripts/make_report.py + reports/周报.xlsx + reports/README.md（都在 xiaoxuanzi-channel）
- 验收证明：周报截图 + 你核对的 3 个数字

**GitHub 关：读懂历史，演练一次撤回**

1. 网页上点开任意提交，看绿色 + 和红色 − 行
2. 在 GitHub Desktop 的 Changes 里看还没提交的改动，在 History 里点最近一次提交看它改了什么
3. 新建 test-revert.md 写错一句，Commit 并 Push origin
4. 在 History 里右键这次提交 → Revert Changes in Commit，看它自动生成一次反向提交，再 Push origin
5. 在网页上确认：内容恢复了，但历史里两次提交都在

- 交付：一次 revert 提交
- 验收证明：Commits 截图，能看到 Revert 那一条

**模型交付**

- ChatGPT：让 ChatGPT 讲懂这份 Excel 周报。把周报里的公式（截图或复制）发给 ChatGPT，让它逐个讲清在算什么；让它出 3 道小题考你，比如「想加一列平均点赞，要改哪里」，你答对为止；让它列出这份报表最容易出错的 3 个地方，交给 Claude Code 写进 reports/README.md 的「常见问题」。交付：讲解记录 + 3 道题的作答 + 常见问题 3 条
- Gemini：看图读数：从截图提取表格。截一张频道规划 Excel 里「每周时间分配」表的图；让 Gemini 把图里的数据提取成 CSV 格式；逐格核对，记下它错了几处；正确的版本交给 Claude Code 存进 practice/。交付：提取出的 CSV + 错误统计
- Grok：找 3 个值得关注的 AI 学习仓库。让 Grok 找 3 个适合零基础学 AI 工具的 GitHub 仓库；每个要链接、Star 数、一句话介绍；你逐个点开核对，存成 docs/值得关注的仓库.md。交付：已核对的仓库清单

**每日安排（主技术块）**

- 周一：Claude Code 配好 Python 环境——让 Claude Code 把 Python 装到 D:\Python、在 xiaoxuanzi-channel 里建 .venv、装好 openpyxl；它要运行的每条命令，看懂用途再批准（验收证明：它最后输出的版本号截图）
- 周二：Gemini 从截图提取表格——按本周 Gemini 交付：截图 → CSV，逐格核对（验收证明：CSV 文件）
- 周三：模拟数据 + 第一版周报——让 Claude Code 生成 sample-data.csv，写 make_report.py，生成 reports/周报.xlsx（验收证明：周报截图）
- 周四：核对数字 + 换数据重做——手动核对 3 个关键数字；让它复制出 sample-data-2.csv 改几行，再生成一次（验收证明：核对记录）
- 周五：查看改动和撤回提交——按本周 GitHub 关，在 GitHub Desktop 里演练一次 Revert Changes in Commit（验收证明：Commits 截图）
- 周六：ChatGPT 讲懂周报 + 使用说明——按本周 ChatGPT 交付做；让 Claude Code 写 reports/README.md（验收证明：对话截图 + README 链接）
- 周日：Grok 仓库清单 + 周复盘——按本周 Grok 交付做；写周复盘（验收证明：文件链接）

- 英语：场景：开会发言
- 视频：可选：记录「AI 帮我做了一张 Excel 周报」

### 第 4 周｜一键 PPT 汇报（11/30–12/06） ⚔️ Boss 周

要交出：从 Excel 报表一键生成可编辑的 PPT；两关都过才算打败 Boss

**Claude Code 关：BOSS：从 Excel 报表一键生成 PPT 汇报**

1. 对 Claude Code 说：「用 python-pptx 写 scripts/make_ppt.py，读 reports/周报.xlsx，生成 reports/周报汇报.pptx」，先让它说明会生成哪几页再动手
2. PPT 要求：10 页以内，有封面、本周关键数字、每周播放量图表、表现最好的 3 条视频、下周计划页（留空给你填），文字都能在 PowerPoint 里直接改
3. 用 PowerPoint 打开，逐页核对：图表和数字与 Excel 一致，没有文字溢出
4. 换模板：把一份你喜欢的 .pptx 放进 templates/，让它再生成一次，确认套用了新模板的配色和字体
5. 让它做一个双击入口 scripts/一键汇报.bat：从 CSV 一路生成 Excel 和 PPT
6. 独立用起来测试：用 sample-data-2.csv，只看 README，自己双击走一遍全程，不问 Claude
7. 可选对比：看看开源工具 ppt-master 的效果（先让 Claude 审核仓库再装），记下哪种更适合你

- 交付：make_ppt.py + 一键汇报.bat + 周报汇报.pptx + 使用说明（都在 xiaoxuanzi-channel）
- 验收证明：PPT 截图 + 你用新数据自己走一遍的截图

**GitHub 关：BOSS：使用说明 + 作品入库**

1. README 加「## Excel 报表和 PPT 汇报怎么用」：放什么数据、双击哪个文件、去哪找结果、出错怎么办
2. 在 GitHub Desktop 里分两次提交：脚本的 Summary 用 feat:，说明文档用 docs:，然后 Push origin
3. 确认 .gitignore 已忽略 .venv；只含模拟数据的示例报表可以提交
4. 网页上打开 make_ppt.py 看代码高亮，点 History 看文件修改历史
5. 给仓库 About 加一句描述和 3 个 Topics

- 交付：README 使用说明 + 脚本和示例报表入库 + About 和 Topics
- 验收证明：仓库链接

**模型交付**

- ChatGPT：写 PPT 讲稿和英文版标题。把周报汇报.pptx 每页的要点发给 ChatGPT；让它为每页写 2–3 句中文讲稿，3 分钟内讲完；再让它把每页标题改成简洁的英文，你挑 3 页用英文讲给它听，让它纠正；讲稿交给 Claude Code 存成 reports/讲稿.md。交付：讲稿.md + 英文标题对照
- Gemini：BOSS 辅助：给 PPT 定配色和版式。把生成的 PPT 截 3 页图发给 Gemini；让它从可读性、配色、图表清晰度给 5 条建议，再给一套主色和字体搭配；挑 2 条交给 Claude Code 改进模板，做前后对比。交付：改进前后对比截图
- Grok：BOSS 辅助：当听众挑刺。把 PPT 讲稿发给 Grok，让它扮演挑剔的领导；让它提 5 个你汇报时可能被追问的问题；你逐个回答，答不上来的交给 Claude Code 补进 PPT 的备注页。交付：5 个追问 + 你的回答

**每日安排（主技术块）**

- 周一：第一版 PPT——让 Claude Code 写 make_ppt.py，从周报.xlsx 生成周报汇报.pptx（验收证明：PPT 截图）
- 周二：逐页核对 + 修正——用 PowerPoint 打开逐页核对数字和图表，有问题交给 Claude Code 修（验收证明：核对记录）
- 周三：Gemini 配色 + 换模板——按本周 Gemini 交付做；放一份模板进 templates/ 再生成一次（验收证明：前后对比截图）
- 周四：ChatGPT 讲稿 + Grok 挑刺——按本周 ChatGPT、Grok 交付做（验收证明：讲稿 + 对话截图）
- 周五：双击入口——让 Claude Code 做 scripts/一键汇报.bat，从 CSV 一路生成 Excel 和 PPT（验收证明：双击后生成的文件截图）
- 周六：BOSS：自己独立走一遍——用 sample-data-2.csv，只看 README，双击入口生成 Excel 和 PPT，不问 Claude（验收证明：生成结果截图）
- 周日：BOSS：使用说明 + 作品入库 + 周复盘——按本周 GitHub 关做；写周复盘（验收证明：仓库链接）

- 英语：场景：写英文邮件
- 视频：可选：记录「AI 把表格变成了汇报 PPT」

### 第 5 周｜网页上线（12/07–12/13）

要交出：一个能用手机打开的网页（GitHub Pages）

**Claude Code 关：写一个英语词卡网页并理解本地服务器**

1. 让 Claude Code 写 index.html：读取 cards.json，一屏一张卡，点击翻面，手机适配
2. 直接双击 index.html，会发现读不出词卡：浏览器不允许本地文件互相读取
3. 对 Claude Code 说「帮我启动本地预览」，它会运行一个本地小服务器并告诉你网址（通常是 http://localhost:8000），用浏览器打开
4. 按 F12 打开开发者工具，看 Console 里有没有报错，让 Claude Code 解释并修掉
5. 让它在 docs/网页笔记.md 里讲清 HTML、CSS、JavaScript 在这个页面里各负责什么

- 交付：index.html + cards.json，本地服务器能正常运行
- 验收证明：localhost 打开的截图

**GitHub 关：用 GitHub Pages 发布网页**

1. 公开前先在 OpenAI 桌面版让 Codex 只读检查一遍：有没有个人信息、链接能不能打开
2. Settings → Pages → Source 选 Deploy from a branch，分支 main，文件夹 / (root)
3. 等网址出现，用手机打开测试翻卡
4. 改一处文字推送，观察多久后网页更新
5. 在 Actions 页面看 pages-build-deployment，理解 Pages 背后也是一次自动运行
6. 把网址发给 1 个朋友试用，记下他卡住或觉得别扭的地方（10 分钟，不计入验收）

- 交付：一个能用手机打开的网址
- 验收证明：网址 + 手机截图

**模型交付**

- ChatGPT：生成并校验 30 张词卡 JSON。规定格式：每张卡有 en、zh、example 三个字段；让 ChatGPT 生成 30 张出差场景词卡，输出 JSON 数组；贴到 jsonlint.com 校验，有错让它修；存成 cards.json。交付：cards.json（校验通过）
- Gemini：给网页挑毛病。用手机截一张网页全图；让 Gemini 从可读性、按钮大小、配色给 5 条建议；挑 2 条交给 Claude Code 改，做前后对比。交付：前后对比截图
- Grok：给网页生成配图。想好网页需要的 3 张图或图标；用 Grok 生成，风格统一；交给 Claude Code 放进网页并调好大小。交付：3 张配图已上线

**每日安排（主技术块）**

- 周一：ChatGPT 生成并校验 JSON——按本周 ChatGPT 交付：30 张词卡 JSON 校验通过（验收证明：校验截图）
- 周二：写词卡网页——让 Claude Code 写 index.html 读 cards.json；双击打开，观察为什么读不出数据（验收证明：截图）
- 周三：本地预览 + 开发者工具——让 Claude Code 启动本地预览并告诉你网址；按 F12 看 Console 有没有报错，交给它修（验收证明：localhost 截图）
- 周四：Gemini 挑毛病并改 2 条——按本周 Gemini 交付做（验收证明：前后对比截图）
- 周五：Grok 配图——按本周 Grok 交付：3 张图放进网页（验收证明：网页截图）
- 周六：Codex 检查 + Pages 上线——先让 Codex 只读检查；再按本周 GitHub 关做，手机打开测试（验收证明：网址）
- 周日：改一处再发布 + 周复盘——改文字推送，在 Actions 页面看 Pages 部署过程；写周复盘（验收证明：Actions 截图）

- 英语：场景：机场值机和过海关
- 视频：可选：「我把一个网页送上线了」

### 第 6 周｜Skill 与命令（12/14–12/20）

要交出：装好现成 Skill + 自定义斜杠命令 + 分支合并

**Claude Code 关：装 Skill + 写自定义斜杠命令**

1. 从 Anthropic 官方 skills 仓库挑一个文件处理类 Skill（如 xlsx）。安装前先审核：通读 SKILL.md 和附带的脚本，写下它会读写哪些文件、会不会联网，确认没问题再复制到 .claude/skills/
2. 重开 Claude Code，问它「你有哪些 Skill」，确认装上，再用它把 sample-data.csv 做成一份格式不同的 Excel，和你第 3 周的周报比一比
3. 在 .claude/commands/ 新建 weekly.md，写一段固定指令（如「运行 一键汇报.bat 并总结本周数据」）
4. 在 Claude Code 里输入 /weekly，看它是否按你的命令执行
5. 把 Skill 和命令的区别写进 docs/skill-与命令.md

- 交付：.claude/skills/ 下的 Skill + .claude/commands/weekly.md + 笔记
- 验收证明：/weekly 运行截图 + 仓库链接

**GitHub 关：分支：新建、切换、合并、删除**

1. GitHub Desktop 顶部点 Current branch → New branch，取名 try-skill
2. 改 README，Commit 后点 Publish branch，网页上能看到两个分支
3. Current branch 切回 main，看 README 变回原样
4. 菜单 Branch → Merge into current branch，选 try-skill 合并，再 Push origin
5. 切到 try-skill，菜单 Branch → Delete 删除分支（勾选同时删除远程分支）

- 交付：一次分支合并
- 验收证明：Commits 截图，能看到合并

**模型交付**

- ChatGPT：description 写法对比。把一个 SKILL.md 开头的 name 和 description 贴给 ChatGPT；让它解释这两项的作用；让它写 5 组好坏对比，说明为什么好的更容易被正确调用；存成 docs/description-写法.md。交付：description-写法.md
- Gemini：把 Skill 画成流程图。复制一个 SKILL.md 全文给 Gemini；让它逐段解释，并画成 Mermaid 流程图；存成 docs/skill-拆解.md，在 GitHub 网页上看流程图能否显示。交付：skill-拆解.md
- Grok：对照两种「技能」写法。复制一个你 Grok 里的 Bot 或指令设置；再找一个 Claude Code 的 SKILL.md；让 Grok 对比触发条件、步骤、限制三部分，做成对照表存进仓库。交付：技能写法对照表.md

**每日安排（主技术块）**

- 周一：读 SKILL.md 结构——打开 anthropics/skills 里一个 SKILL.md，找出 name 和 description，写一句话说明各自用途（验收证明：你的说明）
- 周二：安装现成 Skill 并使用——让 Claude Code 把审核过的 Skill 放进 .claude/skills/；重开确认；用它把 sample-data.csv 做成 Excel（验收证明：产出文件）
- 周三：写第一个斜杠命令——建 .claude/commands/weekly.md，在 Claude Code 里运行 /weekly（验收证明：运行截图）
- 周四：新建和切换分支——按本周 GitHub 关：GitHub Desktop 新建分支、Publish branch、切回 main（验收证明：Branches 页面截图）
- 周五：合并与删除分支——Branch → Merge into current branch、Push origin、Branch → Delete（同时删除远程分支）（验收证明：Commits 截图）
- 周六：Gemini 画 Skill 流程图——按本周 Gemini 交付：Mermaid 流程图在网页上显示（验收证明：文件链接）
- 周日：Grok 对照 + ChatGPT description + 周复盘——按本周 Grok、ChatGPT 交付做；写周复盘（验收证明：文件链接）

- 英语：场景：酒店入住和投诉
- 视频：可选

### 第 7 周｜任务管理（12/21–12/27）

要交出：Issues 管理 + 让 Claude Code 帮你批量建 Issue

**Claude Code 关：让 Claude Code 帮你管理 Issues**

1. 对 Claude Code 说：「帮我装好 GitHub CLI 并登录」，它来运行命令，你只需在弹出的浏览器里点授权
2. 让它按产品大纲建 5 个 Issue，并加上标签
3. 打开网页 Issues 页面，核对 5 个 Issue 都在
4. 完成其中一个后，在 GitHub Desktop 提交时 Summary 写 fixes #编号，点 Push origin 后看这个 Issue 自动关闭
5. 让它把这周用到的操作整理成 docs/issue-速查.md

- 交付：5 个 Issue（由 Claude Code 创建），1 个由提交自动关闭 + Issue 速查表
- 验收证明：Issues 页面截图

**GitHub 关：Labels、Milestones 和 Projects 看板**

1. 建三个标签：技术、产品、视频
2. 建里程碑「12 周 v1.0」，截止 1/31
3. 新建一个 Project 看板，三列：待办、进行中、完成
4. 把本周建的 Issue 全部加进看板，按进度拖动

- 交付：带标签和里程碑的 Issues + 一个看板
- 验收证明：看板截图

**模型交付**

- ChatGPT：用访谈法写产品大纲。让 ChatGPT 当产品经理，一次问一个问题，共 10 个；你逐个回答：目标用户、痛点、内容、形式；让它整理成 product/大纲.md，这份大纲就是本周拆 Issues 的依据。交付：product/大纲.md
- Gemini：给产品大纲配结构图。把产品大纲发给 Gemini；让它画结构图：几部分、给谁用、先做哪个；存进仓库并贴到对应的 Issue。交付：结构图 + Issue
- Grok：同类产品竞品表。让 Grok 找 5 个和你产品方向类似的数字产品；每个记名称、链接、价格、卖点；你逐个核对，存成 product/竞品表.md，写一句你的不同。交付：竞品表.md

**每日安排（主技术块）**

- 周一：Issues 入门——在网页 Issues 页面手动建 1 个 Issue，弄懂标题、描述、标签；再让 Claude Code 装好 GitHub CLI 并登录（它运行命令，你在浏览器里点授权）（验收证明：Issue 截图）
- 周二：ChatGPT 访谈出产品大纲——按本周 ChatGPT 交付做（验收证明：文件链接）
- 周三：让 Claude Code 批量建 Issues——让 Claude Code 按大纲建 5 个 Issue；到网页 Issues 页面核对（验收证明：Issues 截图）
- 周四：Labels、Milestone、看板——按本周 GitHub 关做（验收证明：看板截图）
- 周五：提交自动关闭 Issue——完成一个 Issue，提交说明写 fixes #编号，推送后确认自动关闭（验收证明：关闭的 Issue 截图）
- 周六：Gemini 结构图（可放假期）——按本周 Gemini 交付做（验收证明：Issue 截图）
- 周日：Grok 竞品表 + Issue 速查 + 周复盘——按本周 Grok 交付；整理 Issue 速查表；写周复盘（验收证明：文件链接）

- 英语：场景：打车和问路
- 视频：节日周可停

### 第 8 周｜写出自己的 Skill（12/28–01/03） ⚔️ Boss 周

要交出：自己写的 Skill 经 Pull Request 合并进仓库

**Claude Code 关：BOSS：写出自己的 Skill「脚本润色」**

1. 在 .claude/skills/script-polish/ 新建 SKILL.md
2. 开头 YAML 写 name 和 description，description 写清「什么时候该用它」
3. 正文写：输入、润色步骤、输出格式（润色稿 + 5 个标题）、禁止事项
4. 重开 Claude Code，给一段真实口播稿，看它是否自动调用这个 Skill
5. 按测试用例逐组跑，改到 5 组都符合预期

- 交付：script-polish/SKILL.md + 测试结果
- 验收证明：SKILL.md 截图 + 测试结果

**GitHub 关：BOSS：用 Pull Request 合并你的 Skill**

1. GitHub Desktop 新建分支 skill-script-polish，把 Skill 提交到这个分支并点 Publish branch
2. 点 Create Pull Request（或网页上的 Compare & pull request）发起 PR，写清做什么、怎么测过
3. 在 Files changed 里逐行检查
4. Merge pull request，删除分支
5. README 加「## 我的 Skill」使用说明

- 交付：一个已合并的 PR + 使用说明
- 验收证明：PR 链接

**模型交付**

- ChatGPT：打磨 Skill 规则。把 script-polish 规则草稿贴给 ChatGPT；让它找出模糊、矛盾和漏掉的地方；你决定改哪些，交给 Claude Code 写进 SKILL.md，你在 GitHub Desktop 里提交。交付：SKILL.md 的修改提交
- Gemini：BOSS 辅助：给 Skill 出测试题。把 Skill 规则发给 Gemini；让它出 5 组测试输入，分别检查：保留事实、不改原意、表达自然、换一种语气、异常输入（空文本或乱码），每组写期望输出；存成 docs/skill-测试用例.md，逐组跑并记录实际结果。交付：skill-测试用例.md
- Grok：BOSS 辅助：当挑刺测试员。把 Skill 规则发给 Grok；让它列出 10 种会让 Skill 出错的情况；挑 3 种修进规则，记录修改前后。交付：挑刺清单 + 3 条修改

**每日安排（主技术块）**

- 周一：起草 Skill 规则——写下 script-polish 的输入、步骤、输出、禁止事项、验收点（验收证明：草稿截图）
- 周二：ChatGPT 打磨 → SKILL.md——按本周 ChatGPT 交付做；写成带 name 和 description 的 SKILL.md（验收证明：SKILL.md 截图）
- 周三：安装并试跑——放进 .claude/skills/script-polish/，用真实口播稿试跑（验收证明：输出截图）
- 周四：Gemini 测试用例——按本周 Gemini 交付：5 组用例逐组跑（验收证明：用例文件）
- 周五：Grok 挑刺修 3 条——按本周 Grok 交付做（验收证明：修改截图）
- 周六：BOSS：分支 + PR——按本周 GitHub 关：GitHub Desktop 建分支、Publish branch、Create Pull Request（验收证明：PR 链接）
- 周日：BOSS：合并 PR + 使用说明 + 周复盘——Merge、删分支、README 写使用说明；写周复盘（验收证明：PR 链接）

- 英语：场景：电话会议
- 视频：可停

### 第 9 周｜自动化（01/04–01/10）

要交出：GitHub Actions 每周自动生成周报并提交

**Claude Code 关：让 Claude Code 写一个 GitHub Actions 工作流**

1. 让它解释 GitHub Actions 是什么：在 GitHub 的服务器上按规则自动运行脚本
2. 让它写 .github/workflows/weekly.yml：每周日定时运行 make_report.py，用 sample-data.csv 生成 Excel 周报并自动提交；同时加 workflow_dispatch，让你随时能手动补跑
3. 推送后到仓库 Actions 页面，手动点一次 Run workflow 测试
4. 运行失败就打开日志，把报错发给 Claude Code 修，直到变绿
5. 弄懂 yml 里 on、schedule、jobs、steps 四个部分各是什么

- 交付：weekly.yml + 一次成功的自动运行
- 验收证明：Actions 页面绿色对勾截图

**GitHub 关：读懂 Actions 运行日志和权限**

1. 打开 weekly.yml 的一次运行，逐个展开每一步日志
2. 打开写权限前，先让 Codex 只读检查 weekly.yml 会改哪些文件
3. 理解 Actions 自动提交需要写权限：Settings → Actions → General → Workflow permissions
4. 在 README 顶部加一个工作流状态徽章（badge）
5. 故意改错一行让它失败，看失败邮件和日志，再修好

- 交付：状态徽章 + 一次失败再修复的记录
- 验收证明：README 截图，能看到徽章

**模型交付**

- ChatGPT：解释 YAML 语法。把 weekly.yml 贴给 ChatGPT，让它讲清 YAML 的缩进规则和列表写法；让它出 3 个有错的 YAML 片段，你找出错误；把要点写进 docs/yaml-笔记.md。交付：yaml-笔记.md
- Gemini：让 Gemini 审 Actions 报错。把一次失败运行的日志截图发给 Gemini；让它解释报错原因和修复方法；和 Claude Code 给的方案对比，记下谁说得更准。交付：对比记录
- Grok：AI 圈新闻英文复述。让 Grok 找本周 AI 工具圈 3 条新闻，附来源链接；每条用英文复述 3 句；让它纠错，存成文件。交付：新闻复述.md

**每日安排（主技术块）**

- 周一：Actions 是什么——让 Claude Code 讲清 GitHub Actions；在网页 Actions 页面看 Pages 已经在用的那个工作流（验收证明：一句话说明）
- 周二：写 weekly.yml——让 Claude Code 写定时工作流；推送后手动 Run workflow（验收证明：运行截图）
- 周三：读日志修错误——打开运行日志，失败就把报错发给 Claude Code 修，直到变绿（验收证明：绿色对勾截图）
- 周四：权限 + 徽章——设置 Workflow permissions；README 加状态徽章（验收证明：README 截图）
- 周五：Gemini 审报错——按本周 Gemini 交付做（验收证明：对话截图）
- 周六：ChatGPT 讲 YAML——按本周 ChatGPT 交付做（验收证明：文件链接）
- 周日：等周日自动运行 + Grok 新闻 + 周复盘——周日确认工作流自动跑了一次；按本周 Grok 交付做；写周复盘（验收证明：自动运行记录截图）

- 英语：场景：商务饭局寒暄
- 视频：可选：「仓库每周自己给我写周报」

### 第 10 周｜串起工作流（01/11–01/17）

要交出：Claude Code + GitHub + 至少一个其他模型的可重复工作流

**Claude Code 关：串起一条可重复的工作流**

1. 设计流程：Grok 找资讯 → Gemini 看图提取信息 → Claude Code 汇总成文 → 提交到 GitHub
2. 让 Claude Code 写 scripts/workflow.ps1，把能自动的步骤串起来，手动步骤留输入文件
3. 让 Claude Code 把本周的提交记录也汇总进去（它会自己运行 Git 命令，你看懂结果就行）
4. 真实跑一遍，把每一步的输入输出存档
5. 写 docs/工作流说明.md：步骤、工具、输入、输出、哪一步必须人工审核、出错怎么办；再按说明从头跑第二遍，确认能复现

- 交付：workflow.ps1 + 工作流说明 + 一次完整运行的存档
- 验收证明：工作流说明链接

**GitHub 关：Fork 开源项目，读懂它的结构**

1. 找一个开源 Skill 仓库，Star 并 Fork 到你的账号
2. 用 GitHub Desktop 的 File → Clone repository 把你的 fork 克隆到 D:\GitHub
3. 在 fork 里改一处说明并推送，理解 Fork 和 Clone 的区别
4. 写 docs/开源仓库拆解.md：目录结构、每个文件的作用、3 个可借鉴的地方

- 交付：一个 fork + 拆解文档
- 验收证明：fork 链接 + 文档链接

**模型交付**

- ChatGPT：工作流检查表。把工作流步骤告诉 ChatGPT；让它整理成可打勾的检查表，每步写清输入、工具、输出；存成 docs/工作流检查表.md，下次跑时照着打勾。交付：工作流检查表.md
- Gemini：工作流里负责「看图」一环。工作流里固定一步交给 Gemini：看截图提取信息；写好可复用的提示词；真实跑一次，把提示词和输出存进工作流说明。交付：提示词 + 一次输出
- Grok：工作流里负责「资讯输入」一环。工作流里固定一步交给 Grok：找最新资讯或参考案例；写好可复用的提示词；真实跑一次，存进工作流说明。交付：提示词 + 一次输出

**每日安排（主技术块）**

- 周一：设计工作流——画出步骤：Grok 资讯 → Gemini 看图 → Claude Code 汇总 → 提交（验收证明：步骤图）
- 周二：写 workflow.ps1——让 Claude Code 把能自动的步骤串起来（验收证明：脚本文件）
- 周三：接入 Grok 和 Gemini 两环——按本周 Grok、Gemini 交付写提示词，输出作为脚本输入（验收证明：提示词文件）
- 周四：真实跑一遍——完整运行，存档每一步的输入和输出（验收证明：存档文件夹）
- 周五：Fork 开源仓库——按本周 GitHub 关做（验收证明：fork 链接）
- 周六：工作流说明 + 检查表——写 docs/工作流说明.md；按本周 ChatGPT 交付做检查表（验收证明：文件链接）
- 周日：开源拆解 + 周复盘——写开源仓库拆解；写周复盘（验收证明：文件链接）

- 英语：场景：带客户参观
- 视频：可选：记录这条工作流

### 第 11 周｜作品集与产品（01/18–01/24）

要交出：GitHub 主页作品集 + 产品草稿 v1

**Claude Code 关：把成果整理成产品草稿 v1**

1. 让 Claude Code 扫描整个仓库，列出所有成果和对应技能
2. 在 product/ 下生成章节：每章一项技能，写问题、步骤、你的真实案例、常见坑
3. 生成 product/README.md 总目录，检查每个链接都能点开；每章末尾写「已知限制」
4. 公开前做一次隐私清查：让 Claude Code 搜索整个仓库里的邮箱、手机号、真实姓名、密钥和健康数据，有就删掉或脱敏
5. 让它把 product/ 做成一个网页，挂到 GitHub Pages 的子路径下

- 交付：product/ 文件夹 + 在线网页版
- 验收证明：网页链接

**GitHub 关：GitHub 个人主页作品集**

1. 新建和用户名同名的仓库 derekdye6671-DX，勾 README
2. 这个 README 会显示在你的主页：写自我介绍和 12 周成果列表，配上图片
3. 主页 Customize your pins 置顶 xiaoxuanzi-channel
4. xiaoxuanzi-channel 的 README 改成作品集目录，用相对链接

- 交付：个人主页 README + 置顶
- 验收证明：你的 GitHub 主页链接

**模型交付**

- ChatGPT：写一章完整示例。选产品草稿里最有用的一章；让 ChatGPT 根据你的真实操作记录写从零开始的示例；你照着走一遍，改掉错误后存进 product/。交付：一个验证过的示例章节
- Gemini：写产品说明页。把产品目录发给 Gemini；让它写说明：是什么、适合谁、怎么用，再写 3 个示例；你删掉夸大的话，存进 product/。交付：产品说明.md
- Grok：按终章标准查漏。把终章 6 条标准和仓库目录发给 Grok；让它逐条判断：已达成、部分达成、没做；缺口让 Claude Code 建成 Issues。交付：查漏结果 + Issues

**每日安排（主技术块）**

- 周一：个人主页 README——建同名仓库 derekdye6671-DX，写自我介绍和成果列表（验收证明：主页链接）
- 周二：置顶 + 作品集目录——置顶仓库；README 改成作品集目录，用相对链接（验收证明：主页截图）
- 周三：Claude Code 汇总产品草稿——扫描仓库，在 product/ 生成章节和总目录（验收证明：product 链接）
- 周四：产品网页版——让 Claude Code 把 product/ 做成网页挂到 Pages 子路径（验收证明：网页链接）
- 周五：ChatGPT 示例 + Gemini 说明——按本周两项交付做（验收证明：文件链接）
- 周六：Grok 查漏建 Issues——按本周 Grok 交付：缺口让 Claude Code 建成 Issues（验收证明：Issues 截图）
- 周日：给一个人看 + 周复盘——把产品网页发给一个朋友，记下看不懂的地方并修改；写周复盘（验收证明：修改记录）

- 英语：场景：项目汇报
- 视频：可选：讲产品草稿是怎么来的

### 第 12 周｜终章（01/25–01/31） ⚔️ Boss 周

要交出：v1.0 Release + 12 周复盘 + 下一个 12 周

**Claude Code 关：BOSS：用 git 数据做 12 周复盘**

1. 让 Claude Code 用 git log 统计 12 周：提交总数、每周分布、改动最多的文件
2. 生成 docs/12周复盘.md，带每周提交柱状图
3. 写新的反向愿景和下一个 12 周要学的技术
4. 对照终章 6 条标准逐条自查，缺的补上

- 交付：12周复盘.md + 下一个 12 周计划
- 验收证明：文件链接

**GitHub 关：BOSS：打 v1.0 标签并发布 Release**

1. 清理仓库，检查所有链接能点开
2. 在网页 Releases 点 Draft a new release，Choose a tag 里输入 v1.0 并选 Create new tag
3. 点 Generate release notes，再补 3 句总结
4. 把产品草稿打包成 zip 作为附件上传，Publish release

- 交付：v1.0 Release
- 验收证明：Release 链接

**模型交付**

- ChatGPT：英文 12 周总结讲稿。用中文写 5 个要点；让 ChatGPT 改成 2 分钟英文讲稿，用 B1 水平说得出口的词；让它标出你可能读错的单词，录音并和第 1 天对比。交付：讲稿 + 录音
- Gemini：做 12 周作品集海报。列出 5 个最拿得出手的成果；让 Gemini 设计竖版海报「小玄子的 12 周」；放进仓库和个人主页 README。交付：作品集海报
- Grok：英文 12 周总结彩排。让 Grok 当英文听众，你讲 12 周总结；让它打分并给 3 条改进；改完再讲一遍，保存两次评分。交付：两次评分

**每日安排（主技术块）**

- 周一：git log 统计 12 周——让 Claude Code 统计提交总数、每周分布、改动最多的文件（验收证明：统计结果）
- 周二：写 12 周复盘——生成复盘文档，带每周提交柱状图（验收证明：文件链接）
- 周三：新反向愿景 + 下一个 12 周——写清停下来会怎样；列下一个 12 周要学的技术（验收证明：文件链接）
- 周四：BOSS：打标签发 Release——按本周 GitHub 关：在网页 Releases 创建 v1.0 标签和 Release，上传附件（验收证明：Release 链接）
- 周五：Gemini 海报——按本周 Gemini 交付做（验收证明：主页截图）
- 周六：Grok 和 ChatGPT 英文总结彩排——按本周两项交付做（验收证明：对话截图）
- 周日：终章验收——对照终章 6 条逐条自查，整理所有链接交给 Claude（验收证明：链接清单）

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
| E11 | ffmpeg 入门：让 Claude Code 帮你处理视频 | 视频自动化 | 4 |
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
| E27 | diagram-design：给频道做统一风格的示意图 | 开源工具 | 5 |
| E28 | 拆解 mattpocock/skills，改出你自己的版本 | Claude Code 进阶 | 6 |
| E29 | claude-mem：让 Claude Code 记住上次做了什么 | Claude Code 进阶 | 7 |
| E30 | VoiceStudio：本地配音和转写（先测电脑能不能跑） | 视频自动化 | 8 |
| E32 | 批量改名工具：带预览、日志和回滚 | 视频素材整理 | 4 |

## 想加内容怎么办

ChatGPT 或 Codex 想增加实用类、工具类内容时，按 HANDOFF.md 的模板写成「建议」，写清：放在第几周、替换什么（优先替换，不叠加）、学习者操作用时和 AI 等待时间分开估、交付物和验收证明、对 6 件作品的影响。用户确认后由 Claude 写进冒险岛和本文件，避免出现两份计划。
