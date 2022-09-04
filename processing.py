from bs4 import BeautifulSoup
import json

URL = 'https://www.gunviolencearchive.org/'

def getData(fileName = 'data/dataTable.txt'):
    with open(fileName, 'r') as f:
        tables = f.read()
    return tables

def writeData(data, fileName = 'data/data.json'):
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)

def process(tables):
    
    soup = BeautifulSoup(tables, 'html.parser')

    incidents = []
    for item in soup.select('tr'):

        incident = {}

        fields = item.select('td')
        incident['id'] = fields[0].text
        incident['date'] = fields[1].text
        incident['state'] = fields[2].text
        incident['city'] = fields[3].text
        incident['address'] = fields[4].text
        incident['killed'] = fields[5].text
        incident['injured'] = fields[6].text

        links = fields[7].select('a')
        incident['url'] = URL + links[0]['href']
        incident['source'] = links[1]['href']

        incidents.append(incident)
    
    return incidents

if __name__ == '__main__':
    tables = getData()
    incidents = process(tables)
    writeData(incidents)