import json,sys
P=json.load(open('/home/claude/quest-island/plan.json',encoding='utf8'))
WD=['周一','周二','周三','周四','周五','周六','周日']
def block(lab,T):
    return [f"**{lab}：{T['t']}**",""]+[f"{n+1}. {x}" for n,x in enumerate(T['s'])]+["",f"- 交付：{T['d']}",f"- 验收证明：{T['p']}",""]
def week(i):
    w=P['WEEKS'][i];o=[]
    o+= [f"### 第 {i+1} 周｜{w['t']}（{w['d']}）"+(" ⚔️ Boss 周" if w.get('boss') else ""),""]
    if w.get('hol'): o+=[f"> {w['hol']}",""]
    o+=[f"要交出：{w['del']}",""]
    if w.get('lead'): o+=[f"本周主角 AI：{w['lead']}",""]
    if (P.get('CONTENT') or [None]*12)[i]: o+=block('🎬 内容关（必做）',P['CONTENT'][i])
    for lab,k in [('Claude Code 关','CC'),('GitHub 关（必做）' if (P.get('CONTENT') or [None]*12)[i] else 'GitHub 关','GIT')]:
        o+=block(lab,P[k][i])
    if (P.get('AI') or [None]*12)[i]:
        o+=block('🤖 AI 协作关',P['AI'][i])
    else:
        o+=["**模型交付**",""]
        for lab,k in [('ChatGPT','GPT'),('Gemini','GEM'),('Grok','GROK')]:
            T=P[k][i];o.append(f"- {lab}：{T['t']}。"+"；".join(T['s'])+f"。交付：{T['d']}")
        o.append("")
    if (P.get('PROD') or [None]*12)[i]: o+=block('📦 产品关',P['PROD'][i])
    o+=["**每日安排（今日主任务）**" if P.get('CONTENT') and P['CONTENT'][i] else "**每日安排（主技术块）**",""]
    for j,d in enumerate(P['DAYS'][i]): o.append(f"- {WD[j]}：{d['t']}——{d['s']}（验收证明：{d.get('p','')}）")
    o+=["",f"- 英语：{w['e']}"]
    if not (P.get('CONTENT') and P['CONTENT'][i]): o.append(f"- 视频：{w['v']}")
    if (P.get('CONTENT') or [None]*12)[i]: o.append("- 🏊 游泳：本周累计 ≥2500 米，健身房 ≥2 次")
    o.append("")
    return "\n".join(o)
print(week(int(sys.argv[1])))
