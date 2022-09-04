from playwright.async_api import async_playwright
from playwright._impl._api_types import TimeoutError
import asyncio
import random

URL = 'https://www.gunviolencearchive.org/last-72-hours'

def writeData(tables, fileName = 'data/dataTable.txt'):
    with open(fileName, 'w+') as f:
        for table in tables:
            f.write(table)

async def scrape(waitTime = 2, timeout = 2000):
    tables = []
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        await page.goto(URL, wait_until="networkidle")

        while True:
            tableElement = page.locator('tbody')
            table = await tableElement.inner_html()
            tables.append(table)

            next = page.locator("a[title='Go to next page']").nth(0)
            try:
                await next.wait_for(state='visible',timeout=timeout)
            except TimeoutError:
                break
            await asyncio.sleep(random.random()*waitTime)
            await next.click()

        await browser.close()
    return tables

async def main():
    tables = await scrape()
    writeData(tables)

if __name__ == '__main__':
    asyncio.run(main())