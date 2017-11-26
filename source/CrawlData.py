#this code actually same freedata.py and joewin.py 
#just using class structure


import requests
import pprint
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import sqlite3
import unittest


class Domains():
    def __init__(self):
        self.connect = sqlite3.connect("../output/DomainData.db")

        if self.connect:
            print ("Database Connect Succesfuly..")
        else:
            print ("Database is NOT Connect!!!")

        self.database_select = self.connect.cursor()

    def JoeData(selfs):
        files = open("../input/joeDomain.txt", "w")
        result = []
        resul2 = []
        array2 = ['a']
        for i in tqdm(array2):
            page_elements = {}
            get_url = "http://www.joewein.de/sw/spam-bl-" + str(i) + ".htm"
            response = requests.get(get_url).content
            content = response.decode("iso8859_1")
            soup = BeautifulSoup(content, "lxml")
            table = soup.find_all("blockquote")

            for s in table:
                result.append(s.get_text())
            for t in result:
                parse = t.split("\r\n")
                for k in parse:
                    files.writelines(k + "\n")

        print ("load the data...")
    def WhoisJoe(self):
        all_whois = []
        files = open("../input/doms", "r")
        filess = open("../output/domainlist.txt", "w")
        result = []
        list = files.readlines()
        for det in list:
            result.append(det.strip())
        for key in tqdm(result):
            entry = {}
            url = requests.get("http://api.bulkwhoisapi.com/whoisAPI.php?domain="+key+"&token=7d3f08b98ab9f69ae15060a5b58ef1ee").json()

            try:
                if url['formatted_data']['CreationDate'] != "":
                    entry['result'] = url["formatted_data"]
                    all_whois.append(entry)
            except:
                pass



        keyword=all_whois[2]['result'].keys()
        for i in all_whois:
            for k in keyword:
                filess.write(k + "#" + i['result'][k] + "\n")
            filess.write("#" + "\n")

obj=Domains()

obj.WhoisJoe()
