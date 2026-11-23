import json,sys
P=json.load(open('/home/claude/quest-island/plan.json',encoding='utf8'))
WD=['周一','周二','周三','周四','周五','周六','周日']
def week(i):
    w=P['WEEKS'][i];o=[]
    o+= [f"### 第 {i+1} 周｜{w['t']}（{w['d']}）"+(" ⚔️ Boss 周" if w.get('boss') else ""),""]
    if w.get('hol'): o+=[f"> {w['hol']}",""]
    o+=[f"要交出：{w['del']}",""]
    for lab,k in [('Claude Code 关','CC'),('GitHub 关','GIT')]:
        T=P[k][i];o+=[f"**{lab}：{T['t']}**",""]+[f"{n+1}. {x}" for n,x in enumerate(T['s'])]+["",f"- 交付：{T['d']}",f"- 验收证明：{T['p']}",""]
    o+=["**模型交付**",""]
    for lab,k in [('ChatGPT','GPT'),('Gemini','GEM'),('Grok','GROK')]:
        T=P[k][i];o.append(f"- {lab}：{T['t']}。"+"；".join(T['s'])+f"。交付：{T['d']}")
    o+=["","**每日安排（主技术块）**",""]
    for j,d in enumerate(P['DAYS'][i]): o.append(f"- {WD[j]}：{d['t']}——{d['s']}（验收证明：{d.get('p','')}）")
    o+=["",f"- 英语：{w['e']}",f"- 视频：{w['v']}"]

    o.append("")
    return "\n".join(o)
print(week(int(sys.argv[1])))
