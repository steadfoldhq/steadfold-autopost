import subprocess, tempfile, os
from PIL import Image, ImageDraw, ImageFont
M='/home/claude/steadfold-autopost/media/'; N=M+'recovery-oct22/lockedhour/'
OUT='/home/claude/steadfold-autopost/studio/recovery-oct22/lockedhour/before-after/'
F=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf',34) if os.path.exists('/usr/share/fonts/opentype/inter/Inter-Bold.otf') else ImageFont.load_default()
def fr(v,t):
    o=tempfile.mktemp(suffix='.jpg'); subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',v,'-frames:v','1',o],check=True); return o
def row(paths,h):
    ims=[Image.open(p).convert('RGB') for p in paths]; ims=[i.resize((int(i.width*h/i.height),h)) for i in ims]; return ims
def make(name,before,after,h=700):
    b=row(before,h); a=row(after,h)
    W=max(sum(i.width for i in b)+10*len(b),sum(i.width for i in a)+10*len(a))+20
    c=Image.new('RGB',(W,2*h+150),'#f2f2f2'); d=ImageDraw.Draw(c)
    d.text((20,12),'BEFORE (queued)',fill='#333',font=F); d.text((20,h+82),'AFTER (recovery-oct22)',fill='#E0306C',font=F)
    x=20
    for i in b: c.paste(i,(x,58)); x+=i.width+10
    x=20
    for i in a: c.paste(i,(x,h+128)); x+=i.width+10
    c.save(OUT+name+'.jpg',quality=86)
make('lh-1024-reveal-47-seconds',[M+f'lh-1024-reveal-47-seconds/0{i}.jpg' for i in range(1,6)],[N+f'lh-1024-reveal-47-seconds/0{i}.jpg' for i in range(1,4)],500)
make('lh-ch-1024-5',[M+'stories/lh-ch-1024-5.jpg'],[N+'stories/lh-ch-1024-5.jpg'])
make('lh-1025-climb-one-percent',[M+f'lh-1025-climb-one-percent/0{i}.jpg' for i in range(1,8)],[N+f'lh-1025-monday-handle/0{i}.jpg' for i in range(1,4)],420)
make('lh-oneword-01',[M+f'lh-oneword-01/0{i}.jpg' for i in range(1,4)],[N+f'lh-oneword-02-batch/0{i}.jpg' for i in range(1,4)],500)
for rid in ['lh-reel-1024-lyrics','lh-reel-1025am-planning-fallacy','lh-reel-1025-unpack']:
    ov=M+f'reels/{rid}-s15.mp4'; nv=N+f'reels/{rid}-r1.mp4'
    ts=[0.2,1.5,3.0,5.5,9.5]
    make(rid,[M+f'reels/{rid}-s15-cover.jpg']+[fr(ov,t) for t in ts],[N+f'reels/{rid}-r1-cover.jpg']+[fr(nv,t) for t in ts],600)
print('ok')
