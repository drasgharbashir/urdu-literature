import sys,json,re
# usage: notes.py chapter_prefix  (reads <p>.notes, <p>.nmap.json; appends to <p>.ur/.en into <p>.ur2/.en2)
p=sys.argv[1]
gl=[re.sub(r'^\[\d+\] ','',l) for l in open(p+'.notes').read().strip().split('\n')]
m=json.load(open(p+'.nmap.json'))
assert len(gl)==len(m),(len(gl),len(m))
ur=open(p+'.ur').read().strip()+'\n\n# حواشی\n\n'+'\n\n'.join(f'[{i}] {w}: {g}' for i,((w,_,_),g) in enumerate(zip(m,gl),1))
en=open(p+'.en').read().strip()+'\n\n# Notes\n\n'+'\n\n'.join(f'[{i}] {e}: glossed in the printed footnote as "{t}".' for i,(w,e,t) in enumerate(m,1))
open(p+'.ur2','w').write(ur+'\n'); open(p+'.en2','w').write(en+'\n')
