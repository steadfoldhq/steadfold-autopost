import glob,io,os
from playwright.sync_api import sync_playwright
from PIL import Image
CH=glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
I={ # 24x24 stroke icons
 'star':'<path d="M12 2.8l2.8 5.8 6.4.9-4.6 4.5 1.1 6.3L12 17.3l-5.7 3 1.1-6.3-4.6-4.5 6.4-.9z"/>',
 'calc':'<rect x="5" y="2.5" width="14" height="19" rx="2.5"/><path d="M8.5 6.5h7M8.5 11h.01M12 11h.01M15.5 11h.01M8.5 14.5h.01M12 14.5h.01M15.5 14.5h.01M8.5 18h.01M12 18h3.5"/>',
 'cal':'<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4M8 14h2M12 14h2M8 17h2"/>',
 'gift':'<path d="M12 3v18"/><rect x="3" y="8" width="18" height="4.5" rx="1"/><path d="M5 12.5V21h14v-8.5"/><path d="M12 8C9 8 7.5 6.8 7.5 5.3S9.5 3 12 8zM12 8c3 0 4.5-1.2 4.5-2.7S14.5 3 12 8z"/>',
 'lock':'<rect x="4.5" y="10.5" width="15" height="10.5" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/><path d="M12 14.5v3"/>',
 'one':'<path d="M9 7.5l3.5-3V20M8.5 20h7.5"/>',
 'check':'<rect x="4" y="3.5" width="16" height="17" rx="2.5"/><path d="M8 9l2 2 3.5-3.5M8 15.5h8"/>',
 'chat':'<path d="M4 5.5h16v10H10l-4.5 4v-4H4z"/><path d="M8 9.5h8M8 12.5h5"/>',
 'eye':'<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
 'shield':'<path d="M12 3l7.5 3v5.5c0 4.6-3.2 8.2-7.5 9.5-4.3-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M9 12l2 2 4-4"/>',
 'moon':'<path d="M19.5 14.5A8 8 0 0 1 9.5 4.5a8 8 0 1 0 10 10z"/>',
 'drop':'<path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11z"/>',
 'heart':'<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/>',
 'down':'<path d="M12 4v12M7 11.5l5 5 5-5M5 20h14"/>',
}
P={
 'fullyfunded':dict(bg='#2B3FE0',ring='#FF6A3D',ink='#FFFFFF',dot='rgba(255,255,255,.10)',items=[('start-here','star'),('example-math','calc'),('26-paydays','cal'),('free-tools','down')]),
 'lockedhour':dict(bg='#FFE27A',ring='#FF5CA8',ink='#141414',dot='rgba(20,20,20,.12)',items=[('start-here','star'),('lock-in-90','lock'),('one-word','one'),('free-tracker','check')]),
 'hourback':dict(bg='#5E54C9',ring='#FFC94D',ink='#FFFFFF',dot='rgba(255,255,255,.09)',items=[('start-here','star'),('prompts','chat'),('real-runs','eye'),('privacy','shield')]),
 'littlefold':dict(bg='#FFD6E3',ring='#D9497A',ink='#D9497A',dot='rgba(122,33,73,.10)',items=[('start-here','star'),('sleep','moon'),('feeding','drop'),('small-wins','heart')]),
}
html=lambda b,ic: f'''<html><body style="margin:0;width:1080px;height:1920px;background:radial-gradient(circle,{b['dot']} 3px,transparent 3.6px) 0 0/44px 44px,{b['bg']};display:flex;align-items:center;justify-content:center">
<div style="width:560px;height:560px;border-radius:50%;border:22px solid {b['ring']};display:flex;align-items:center;justify-content:center;box-sizing:border-box;background:{'#FFF4E0' if b['bg']=='#FFD6E3' else 'transparent'}">
<svg width="300" height="300" viewBox="0 0 24 24" fill="none" stroke="{b['ink']}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{I[ic]}</svg></div></body></html>'''
os.makedirs('out',exist_ok=True)
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CH); pg=br.new_page(viewport={'width':1080,'height':1920},device_scale_factor=2)
    for acct,b in P.items():
        for name,ic in b['items']:
            pg.set_content(html(b,ic)); pg.wait_for_timeout(100)
            im=Image.open(io.BytesIO(pg.screenshot())).convert('RGB').resize((1080,1920),Image.LANCZOS)
            im.save(f'out/{acct}-{name}.png')
    br.close()
# contact sheet
fs=sorted(glob.glob('out/*.png')); W,H=180,320
sh=Image.new('RGB',(W*4,H*4),'white')
for k,f in enumerate(fs):
    acct=os.path.basename(f).split('-')[0]
    row=list(P).index(acct); col=[n for n,_ in P[acct]['items']].index(os.path.basename(f)[len(acct)+1:-4])
    sh.paste(Image.open(f).resize((W,H)),(col*W,row*H))
sh.save('sheet.jpg'); print(len(fs))
