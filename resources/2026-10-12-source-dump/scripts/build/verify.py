import re,sys,collections
def parse(p):
    txt=open(p,encoding='utf-8').read()
    blocks=re.split(r'\n\s*\n',txt.strip())
    cues=[]
    for b in blocks:
        lines=b.strip().split('\n')
        m=None
        for i,l in enumerate(lines):
            m=re.match(r'(\d\d):(\d\d):(\d\d)[,.](\d\d\d)\s*-->\s*(\d\d):(\d\d):(\d\d)[,.](\d\d\d)',l)
            if m:
                s=int(m[1])*3600+int(m[2])*60+int(m[3])+int(m[4])/1000
                e=int(m[5])*3600+int(m[6])*60+int(m[7])+int(m[8])/1000
                cues.append((s,e,' '.join(lines[i+1:]).strip(),lines[0] if i>0 else ''))
                break
    return cues
def fmt(t):
    h=int(t//3600);m=int((t%3600)//60);s=t%60
    return f"{h:02d}:{m:02d}:{s:06.3f}"
p=sys.argv[1]
c=parse(p)
print("file",p,"cues",len(c))
print("first_start",fmt(c[0][0]) if c else None,"last_end",fmt(c[-1][1]) if c else None)
# longest run of identical consecutive texts
best=(0,None,None);run=1
for i in range(1,len(c)):
    if c[i][2]==c[i-1][2]:
        run+=1
        if run>best[0]: best=(run,c[i-run+1][0],c[i][1],c[i][2])
    else: run=1
if c and best[0]==0: best=(1,None,None,None)
print("max_consecutive_identical",best[0],"at",fmt(best[1]) if best[1] is not None else None,"-",fmt(best[2]) if best[2] is not None else None,"text=",(best[3] or '')[:100])
# gaps
gaps=[(c[i][0]-c[i-1][1],i) for i in range(1,len(c))]
gaps.sort(reverse=True)
for g,i in gaps[:5]:
    print("gap %.1fs before cue %d at %s prev_end=%s text=%r"%(g,i,fmt(c[i][0]),fmt(c[i-1][1]),c[i][2][:80]))
print("FIRST5")
for x in c[:5]: print(fmt(x[0]),'-->',fmt(x[1]),'|',x[2][:200])
print("LAST5")
for x in c[-5:]: print(fmt(x[0]),'-->',fmt(x[1]),'|',x[2][:200])
