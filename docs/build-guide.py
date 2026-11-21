# Builds docs/Busy-Bodies-User-Guide.pdf from docs/user-guide.html.
# Refresh screenshots first (optional): serve the repo on :8765 and run docs/capture.py.
import asyncio, pathlib
from playwright.async_api import async_playwright
ROOT = pathlib.Path(__file__).resolve().parent
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await b.new_page()
        await pg.goto((ROOT/'user-guide.html').as_uri()); await pg.wait_for_timeout(800)
        await pg.pdf(path=str(ROOT/'Busy-Bodies-User-Guide.pdf'), format='Letter', print_background=True, prefer_css_page_size=True,
                     display_header_footer=True, header_template='<span></span>',
                     footer_template='<div style="font-size:8px;color:#8a949c;width:100%;text-align:center;font-family:Arial">Busy Bodies User Guide · <span class="pageNumber"></span> / <span class="totalPages"></span></div>')
        await b.close()
asyncio.run(main())
