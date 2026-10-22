import sys
f,pairs=sys.argv[1],sys.argv[2]
ur=open(f+'.ur2').read(); en=open(f+'.en2').read()
for line in open(pairs).read().strip().split('\n'):
    u,e=line.split(' || ')
    assert ur.count(u)==1,('ur',u,ur.count(u)); assert en.count(e)==1,('en',e,en.count(e))
    ur=ur.replace(' '+u,'\n\n'+u) if ' '+u in ur else ur.replace(u,'\n\n'+u)
    en=en.replace(' '+e,'\n\n'+e) if ' '+e in en else en.replace(e,'\n\n'+e)
open(f+'.ur2','w').write(ur); open(f+'.en2','w').write(en)
def blocks(t):
    t=t.strip().split('\n\n'); return [(b.startswith('# '),len(b.split('\n'))) for b in t]
print(len(blocks(ur)),len(blocks(en)),blocks(ur)==blocks(en))
