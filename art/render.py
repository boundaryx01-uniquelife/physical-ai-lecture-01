import asyncio,sys,os
from scenes import S
from playwright.async_api import async_playwright
async def main():
    os.makedirs('png',exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for k,v in S.items():
            open(f'png/{k}.svg','w').write(v)
            import re
            m=re.search(r'width="(\d+)" height="(\d+)"',v);w,h=int(m[1]),int(m[2])
            pg=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=2)
            await pg.set_content(f'<html><body style="margin:0;background:transparent">{v}</body></html>')
            await pg.screenshot(path=f'png/{k}.png',omit_background=True)
            await pg.close()
        await b.close()
asyncio.run(main())
