from playwright.async_api import async_playwright
import asyncio

URL = 'https://www.gunviolencearchive.org/last-72-hours'
 
async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="networkidle")

        tableElement = page.locator('tbody')
        table = await tableElement.inner_html()
        await browser.close()

        with open('dataTable.html', 'w') as f:
            f.write(table)

if __name__ == '__main__':
    asyncio.run(main())