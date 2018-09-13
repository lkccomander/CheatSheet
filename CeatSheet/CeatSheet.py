import random
import pymongo
from CCMPcode import CCMPcode
from class2 import class2
from Conn import Conn
from pymongo import MongoClient
import pprint

#https://hackernoon.com/turning-vs-code-into-a-killer-mongodb-admin-tool-2514f1596a6c
#https://code.visualstudio.com/docs/python/python-tutorial

#C:\Users\Andres_2\source\repos\CeatSheet\CeatSheet\Conn.py
#C:\Users\Andres_2\source\repos\CeatSheet\CeatSheet\CCMPcode.py

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#mongodb+srv://m001-student:<PASSWORD>@cluster0-0njxn.mongodb.net/test?retryWrites=true
#client = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
#db = client.CheatSheet

#print(client.list_database_names())

#print(db.list_collection_names())exit


db = "CheatSheet"

print("This would create first object of CCMP class 2")

#miConexion = Conn("CheatSheet")
#miConexion.closeConexion()



#mycol = db["CheatSheet"]

#for x in mycol.find():
# print(x)

print("This line will be printed.")
print("------------------------------------------------------------------")

print("This would create first object of CCMP class")
ccmpCode1 = CCMPcode("test1","Cat1",200)
ccmpCode1.displayCCMPcode()

print("This would create first object XX of CCMP class")
ccmpCode2 = Conn("CheatSheet","123")
print("-------------------------------KAROL La Niña de las flores-1--------------------------------")
ccmpCode2.getall()
print("-------------------------------KAROL La Niña de las flores-2--------------------------------")
ccmpCode2.setDB(db)
print("-------------------------------KAROL La Niña de las flores-3--------------------------------")
print(ccmpCode2.db)
print("-------------------------------KAROL La Niña de las flores-4--------------------------------")
#ccmpCode2.getDB(db)
print("-------------------------------KAROL La Niña de las flores---------------------------------")
#pcode = 100
#ccmpCode2.return_code(pcode)
print("-------------------------------KAROL La Niña de las flores---------------------------------")

pcode = 1800
json_codes = ccmpCode2.return_code(pcode)

#https://www.mydatahack.com/how-to-get-data-from-mongodb-with-python/
test = ccmpCode2.return_code(pcode)

for i in test:
<<<<<<< HEAD
    print(" posicion de test" + i.replace()),
=======
    print(" posicion de test:" + i),
>>>>>>> d1122d1fba74af8e2f59a92ffd93a543b76eaeee


#Web server http://bottlepy.org/docs/dev/

#miConexion = Conn("CheatSheet","123")
#miConexion.closeConexion()
