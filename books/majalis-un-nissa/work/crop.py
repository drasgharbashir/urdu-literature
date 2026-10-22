import sys
from PIL import Image, ImageOps
src,dst,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
im=Image.open(src).convert('L')
bb=ImageOps.invert(im).point(lambda v:255 if v>80 else 0).getbbox()
im=im.crop(bb); w,h=im.size
step=h/n
for i in range(n):
    a=max(0,int(i*step)-25); b=min(h,int((i+1)*step)+25)
    im.crop((0,a,w,b)).save(f'{dst}_{i+1}.png')
