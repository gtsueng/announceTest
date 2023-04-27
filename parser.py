import json
import os
import requests

from biothings import config
logger = config.logger

def load_filenames():
    r = requests.get('https://raw.githubusercontent.com/gtsueng/covid_announcements/main/San%20Diego%20County/data/processed_list.txt')
    reportlist=r.text.split('\n')
    formattedlist = [x.replace(" ","%20") for x in reportlist]
    return(formattedlist)

def load_annotations():
    basejsonurl = 'https://raw.githubusercontent.com/gtsueng/covid_announcements/main/San%20Diego%20County/data/processed/'
    formattedlist = load_filenames()
    for eachjson in formattedlist:
        fileurl = os.path.join(basejsonurl,eachjson)
        rawdoc = requests.get(fileurl)
        try:
            doc = json.loads(rawdoc.text)
            doc['_id'] = eachjson.replace('.json','')
            yield doc
        except:
            pass

if __name__ == '__main__':
    with open('output.json', 'w') as output:
        json.dump([i for i in load_annotations()], output)