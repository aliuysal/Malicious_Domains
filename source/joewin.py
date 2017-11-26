#this code writes all malicious domains in joeDomain.txt 
 


import requests
import pprint
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

pp=pprint.PrettyPrinter(indent=4)
files = open("../input/joeDomain.txt", "w")
result=[]
resul2=[]
#array=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
array2=['a']
for i in tqdm(array2):
    page_elements={}
    get_url="http://www.joewein.de/sw/spam-bl-"+str(i)+".htm"
    response = requests.get(get_url).content
    content = response.decode("iso8859_1")
    soup = BeautifulSoup(content, "lxml")
    table=soup.find_all("blockquote")

    for s in table:
        result.append(s.get_text())
    for t in result:
        parse=t.split("\r\n")
        for k in parse:
            files.writelines(k+"\n")


print ("load the data...")
