import json
import requests

from biothings import config
logger = config.logger

def load_filenames():
    r = requests.get('https://github.com/gtsueng/covid_announcements/blob/main/San%20Diego%20County/data/processed_list.txt')
    reportlist=r.text.split('\n')
    formattedlist = [x.replace(" ","%20") for x in reportlist]
    return(formattedlist)

def load_annotations():
    basejsonurl = 'https://github.com/gtsueng/covid_announcements/tree/main/San%20Diego%20County/data/processed/'
    formattedlist = load_filenames()
    for eachjson in formattedlist:
        fileurl = basejsonurl+eachjson
        rawdoc = requests.get(fileurl)
        doc = json.loads(rawdoc.text)
        doc['_id'] = eachjson.replace('.json','')
        yield doc

if __name__ == '__main__':
    with open('output.json', 'w') as output:
        json.dump([i for i in load_annotations()], output)