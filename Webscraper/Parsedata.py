import requests
from bs4 import BeautifulSoup
FULL_NAME = 'Shamia Shanaha'
class SIScraper():
    def __init__(self):
        self.session = requests.Session()
        self.prefix = ''
    
    def retrieveRecords(self, url: str):  # -> Generator[bs4.Tag]
        while url:
            self.prefix = url[:url.rfind('?') + 1]
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            for tag in soup.find_all('div', {"class": "record"}):
                yield tag
            url = self.nextUrl(soup)

    def nextUrl(self, soup):
        for a in soup.select('div.pagination a'):
            if a.text.strip() == 'next':
                return f'{self.prefix}{a["href"]}'
        return None


URL = 'https://collections.si.edu/search/results.htm?date.slider=&q=&dsort=&fq=object_type%3A%22Outdoor+sculpture%22&fq=data_source%3A%22Art+Inventories+Catalog%2C+Smithsonian+American+Art+Museum%22&fq=date:%221400s%22'
scraper = SIScraper()


records = scraper.retrieveRecords(URL)
print('>>>>> TASK 1:', FULL_NAME)
for i, record in enumerate(records, 1):
    print(i, record.find('h2').text)
