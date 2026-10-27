import asyncio,re,os
from scenes2 import S2
from playwright.async_api import async_playwright
async def main():
    os.makedirs('png2',exist_ok=True)
    async with async_playwright() as p:
        br=await p.chromium.launch()
        for k,v in S2.items():
            open(f'png2/{k}.svg','w').write(v)
            m=re.search(r'width="(\d+)" height="(\d+)"',v);w,h=int(m[1]),int(m[2])
            pg=await br.new_page(viewport={'width':w,'height':h},device_scale_factor=2)
            await pg.set_content(f'<html><body style="margin:0;background:transparent">{v}</body></html>')
            await pg.screenshot(path=f'png2/{k}.png',omit_background=True)
            await pg.close()
        await br.close()
asyncio.run(main())
from PIL import Image
import glob
names=sorted(glob.glob('png2/*.png'))
sheet=Image.new('RGB',(3*640,2*480),(255,255,255))
for i,f in enumerate(names):
    im=Image.open(f).convert('RGBA'); im.thumbnail((640,480))
    sheet.paste(im,((i%3)*640,(i//3)*480),im)
sheet.save('sheet2.png');print(names)
