from bs4 import BeautifulSoup
import json

URL = 'https://www.gunviolencearchive.org/'

def main():

    with open("data/dataTable.txt", "r") as f:
        tables = f.read()
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

    with open('data/data.json', 'w') as f:
        json.dump(incidents, f, indent=4)

if __name__ == '__main__':
    main()