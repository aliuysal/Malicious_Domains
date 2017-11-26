#this code saving whois output to database 

import sqlite3

connect = sqlite3.connect("../output/dub.db")

if connect:
    print ("Database Connect Succesfuly..")
else:
    print ("Database is NOT Connect!!!")

database_select = connect.cursor()

def InsertData():
    database_select.execute(''' 
    CREATE TABLE IF NOT EXISTS domain_result(
    RegistrarEmail  TEXT,
    DNSSEC TEXT,
    Lastdatabase TEXT,
    RegistrarURL TEXT,
    RegistrarIANAID NUMERİC,
    DomainStatus TEXT,
    RegistryID TEXT,
    RegistrarServer TEXT,
    DomainName TEXT,
    Registrar TEXT,
    CreationDate NUMERİC,
    RegistrarPhone NUMERİC       
    )
    ''')
    connect.commit()
    print ("Build Database ..")


    files = open("../output/domainlist.txt","r")
    list=files.readlines()
    result=[]

    for i in list:
       parse=i.split("#")
       #print (parse[1].strip())
       result.append(parse[1].strip())
    sayac=0
    while(sayac<=len(result)-1):
        database_select.execute('''insert into domain_result(RegistrarEmail,DNSSEC,Lastdatabase,RegistrarURL,RegistrarIANAID,DomainStatus,RegistryID,RegistrarServer,DomainName,Registrar,CreationDate,RegistrarPhone) values(?,?,?,?,?,?,?,?,?,?,?,?)''',(result[sayac+0], result[sayac+1], result[sayac+2], result[sayac+3], result[sayac+4], result[sayac+5], result[sayac+6], result[sayac+7], result[sayac+8], result[sayac+9], result[sayac+10], result[sayac+11]))
        connect.commit()
        #print(result[sayac+0], result[sayac+1], result[sayac+2], result[sayac+3], result[sayac+4], result[sayac+5], result[sayac+6], result[sayac+7], result[sayac+8], result[sayac+9], result[sayac+10], result[sayac+11]+"\n")
        sayac=sayac+13

    print("Add to whois datas in domain_result table")


InsertData()

