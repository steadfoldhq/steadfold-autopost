import sys; sys.argv=[sys.argv[0]]+sys.argv[1:]
import ff_reels as F
from kit import render_frames, sheet, make_readable
W='/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad/ff/prev'
for rid in sys.argv[1:]:
    r=F.build(rid,W,qa_only=True)
    ts=[0,0.6,2.0,3.0,4.5,6.0,8.0,9.0,11.0,13.0,14.5]
    fr=[int(t*30) for t in ts if t*30<r.duration*30]
    fdir,n=render_frames(r,f"{W}/{rid}",dsf=1,only=fr)
    sheet(fdir,[f/30 for f in fr],f"{W}/{rid}-prev.jpg",cols=6,scale=0.3)
