import json 
class SIScraperJson(SIScraper):

    
    def retrieveRecordsAsJson(self, url):
        yield from map(self.toJson, self.retrieveRecords(url))

    ### You must complete the following method that takes
    ### record of type bs4.Tag (from Task 1), and return a string
    def toJson(self, record):
        dictonary={}
        dictonary['Label']=record.find('h2').text
        for dl in record.find_all('dl'):
          temp_list=[]
          for dd in dl.find_all('dd'):
            temp_list.append(dd.text.split('\xa0')[0].strip())
          dictonary[dl.find('dt').text]=temp_list
        return json.dumps(dictonary)

URL = 'https://collections.si.edu/search/results.htm?date.slider=&q=&dsort=&fq=object_type%3A%22Outdoor+sculpture%22&fq=data_source%3A%22Art+Inventories+Catalog%2C+Smithsonian+American+Art+Museum%22&fq=date:%221400s%22'
scraper = SIScraperJson()
records = scraper.retrieveRecordsAsJson(URL)
print('>>>>> TASK 2:', FULL_NAME)

print('\n>> The FIRST record')
display(next(records))

print('\n>> The LAST record')
display(max(enumerate(records))[1])
