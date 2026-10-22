import re,sys
SP={'آ':'آتوجی','م ب':'محمودہ بیگم','م':'محمودہ بیگم','ب ب':'بڑی بیگم','م ز':'مریم زمانی'}
src=open(sys.argv[1]).read()
pages=re.split(r'^\[p(\d+)\]\n',src,flags=re.M)[1:]
blocks=[]; notes=[]
newstart=lambda l: l.startswith('#') or re.match(r'^(آ|م ب|م|ب ب|م ز): ',l)
for i in range(0,len(pages),2):
    pn=int(pages[i]); lines=[l for l in pages[i+1].split('\n') if l.strip()]
    fns={}
    for l in lines:
        m=re.match(r'^\{fn(\d+)\} (.*)',l)
        if m: fns[m.group(1)]=m.group(2)
    body=[l for l in lines if not l.startswith('{fn')]
    def rep(m):
        notes.append((pn,fns.get(m.group(1),'?'))); return f' [{len(notes)}]'
    body=[re.sub(r'\{(\d+)\}',rep,l) for l in body]
    for j,l in enumerate(body):
        if j==0 and blocks and not newstart(l) and not blocks[-1].startswith('#'):
            blocks[-1]=blocks[-1]+' '+l
        else: blocks.append(l)
out=[]
for b in blocks:
    m=re.match(r'^(آ|م ب|م|ب ب|م ز): (.*)',b)
    if m: b=SP[m.group(1)]+': '+m.group(2)
    if b.startswith('## '): b=b[3:]
    out.append(b)
for n,(pn,t) in enumerate(notes,1):
    pass
open(sys.argv[2],'w').write('\n\n'.join(out)+'\n')
open(sys.argv[3],'w').write('\n'.join(f'[{n}] {t}' for n,(pn,t) in enumerate(notes,1))+'\n')
