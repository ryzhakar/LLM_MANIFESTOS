import hashlib, os, re, shutil, subprocess, datetime
SCRATCH = os.environ.get("SOURCE_PULL_SCRATCH", "/tmp/source-pull")
TR=SCRATCH+'/transcripts'; AU=SCRATCH+'/audio'; RP=SCRATCH+'/reports'
REPO='/Users/ryzhakar/LLM_MANIFESTOS/resources/2026-10-12-source-dump/primary'
MW='/Users/ryzhakar/Applications/MacWhisper.app/Contents/MacOS/mw'
MODEL='parakeet-pro:nvidia_parakeet-v3'
items=[('S-02','2OMRWPOSw9s','S-02-2OMRWPOSw9s',2852,'47:32'),
       ('S-03','W2tWOdzgXHA','S-03-W2tWOdzgXHA',4632,'1:17:12'),
       ('S-04','b4p_tcLYDV0','S-04-b4p_tcLYDV0',4848,'1:20:48')]
timing={'2OMRWPOSw9s':(42,20),'W2tWOdzgXHA':(32,31),'b4p_tcLYDV0':(34,34)}
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def ts(s):
    s=float(s); return '%02d:%02d:%06.3f'%(int(s//3600),int((s%3600)//60),s%60)
def parse_srt(p):
    txt=open(p,encoding='utf-8').read()
    cues=[]
    for b in re.split(r'\n\s*\n',txt.strip()):
        L=b.strip().split('\n')
        for i,l in enumerate(L):
            m=re.match(r'(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)',l)
            if m:
                s=int(m[1])*3600+int(m[2])*60+int(m[3])+int(m[4])/1000
                e=int(m[5])*3600+int(m[6])*60+int(m[7])+int(m[8])/1000
                cues.append((s,e,' '.join(L[i+1:]).strip())); break
    return cues
def maxrun(seq):
    best=(0,0);run=0;prev=object();end=None
    for i,x in enumerate(seq):
        run = run+1 if x==prev else 1
        prev=x
        if run>best[0]: best=(run,i)
    return best
report=[]
for sid,vid,folder,dur,dstr in items:
    srt=f'{TR}/{vid}.srt'; txt=f'{TR}/{vid}.txt'; au=f'{AU}/{vid}.m4a'
    cues=parse_srt(srt); last_end=cues[-1][1]; gap=dur-last_end
    run,endi=maxrun([c[2] for c in cues])
    runstart=cues[endi-run+1][0] if run else 0
    runend=cues[endi][1] if run else 0
    words=len(open(txt,encoding='utf-8').read().split())
    lines=[l.strip() for l in open(txt,encoding='utf-8').read().split('\n') if l.strip()]
    trun,_=maxrun(lines)
    status='FULL' if (abs(gap)<=60 and run<=3) else 'PARTIAL'
    reason='' if status=='FULL' else f'last cue end {last_end:.1f}s vs duration {dur}s; longest repeat {run}'
    # metadata
    rep=open(f'{RP}/video-{vid}.md',encoding='utf-8').read()
    def field(name):
        m=re.search(r'^- '+name+r': (.*)$',rep,re.M); return m[1].strip() if m else 'NOT FOUND'
    title=field('title'); chan=field('channel'); up=field('upload_date'); url=field('webpage_url')
    up_fmt=f'{up[:4]}-{up[4:6]}-{up[6:]}' if re.fullmatch(r'\d{8}',up) else up
    today=subprocess.run(['date','+%F'],capture_output=True,text=True).stdout.strip()
    cmd_base=f'{MW} transcribe {au} --format {{fmt}} --language en --model {MODEL} -o {TR}/{vid}.{{fmt}} --overwrite'
    cmds='\n'.join('  '+cmd_base.format(fmt=f) for f in ('srt','txt'))
    rs,rt=timing[vid]
    dest=f'{REPO}/{folder}'
    cp_srt=f'{dest}/{vid}-transcript.srt'; cp_txt=f'{dest}/{vid}-transcript.txt'
    shutil.copy2(srt,cp_srt); shutil.copy2(txt,cp_txt)  # cp -p equivalent (preserves mode and times)
    h_s,h_t=sha(srt),sha(txt)
    ok=(sha(cp_srt)==h_s and sha(cp_txt)==h_t)
    if not ok: raise SystemExit(f'SHA MISMATCH {vid}')
    side=f'''ID: {sid}
VIDEO ID: {vid}
TITLE: {title}
CHANNEL: {chan}
UPLOAD DATE: {up_fmt}
DURATION: {dur} s ({dstr})
URL: {url}
SOURCE AUDIO: {au} ({os.path.getsize(au)} bytes, sha256 {sha(au)})
TRANSCRIBER: MacWhisper 15.0.1 (1502) via bundled mw CLI ({MW})
MODEL: {MODEL}
LANGUAGE: en
COMMANDS:
{cmds}
  (run order: srt then txt; each run wall-clock {rs} s srt, {rt} s txt)
DATE: {today}
TRANSCRIPT {vid}-transcript.srt: sha256 {h_s}; cues {len(cues)}; last cue end {ts(last_end)}
TRANSCRIPT {vid}-transcript.txt: sha256 {h_t}; words {words}
STATUS: {status}{(' - '+reason) if reason else ''}
'''
    open(f'{dest}/{vid}-transcript-provenance.txt','w',encoding='utf-8').write(side)
    report.append(dict(sid=sid,vid=vid,folder=folder,dur=dur,last=last_end,gap=gap,cues=len(cues),run=run,runtxt=f'{ts(runstart)}-{ts(runend)}' if run else '',words=words,trun=trun,status=status,h_s=h_s,h_t=h_t,ok=ok,au_sha=sha(au),au_bytes=os.path.getsize(au),rs=rs,rt=rt))
    print(vid,'copied, sha match:',ok,'status',status,'cues',len(cues),'last',ts(last_end),'run',run,'words',words,'txt-run',trun)
import json; json.dump(report,open(SCRATCH+'/work/report.json','w'),indent=1)
