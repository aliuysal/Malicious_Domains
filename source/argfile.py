#this code whois queries of malicious domains 

import sys
import requests
from tqdm import tqdm


arguman=sys.argv[1]
all_whois=[]
files=open(arguman)
dizi=files.readlines()

filess=open("../output/domainlist.txt","w")
result=[]
for det in dizi:
    result.append(det.strip())
for key in tqdm(result):
    entry = {}
    url = requests.get(
            "http://api.bulkwhoisapi.com/whoisAPI.php?domain={0}&token=7d3f08b98ab9f69ae15060a5b58ef1ee".format(
                key)).json()

    try:
        if url['formatted_data']['CreationDate'] != "":
            entry['result'] = url["formatted_data"]
            all_whois.append(entry)
    except:
        pass
print (all_whois)
keyword = all_whois[0]['result'].keys()
for i in all_whois:
    for k in keyword:
        filess.write(k + "||" + i['result'][k] + "\n")
    filess.write("#" + "\n")



