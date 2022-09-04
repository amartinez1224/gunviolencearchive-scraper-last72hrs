from playwright.async_api import async_playwright
import asyncio
import random
import json

def getData(fileName = 'data/data.json'):
    with open(fileName, 'r') as f:
        items = json.load(f)
    return items

def writeData(data, fileName = 'data/dataRawDetail.json'):
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)

async def scrapeDetail(incidents, waitTime = 1):
    data = {}
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        
        for incident in incidents:
            await page.goto(incident['url'], wait_until="networkidle")
            tableElement = page.locator("div[class='block block-system']")
            text = await tableElement.inner_html()
            data[incident['id']] = text
            await asyncio.sleep(random.random()*waitTime)

        await browser.close()
    return data

async def main():
    incidents = getData()
    data = await scrapeDetail(incidents)
    writeData(data)

if __name__ == '__main__':
    asyncio.run(main())