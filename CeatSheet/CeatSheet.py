from CCMPcode import CCMPcode
from class2 import class2
from Conn import Conn
import random
import pymongo

#C:\Users\Andres_2\source\repos\CeatSheet\CeatSheet\Conn.py
#C:\Users\Andres_2\source\repos\CeatSheet\CeatSheet\CCMPcode.py

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#mongodb+srv://m001-student:<PASSWORD>@cluster0-0njxn.mongodb.net/test?retryWrites=true
#client = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
#db = client.CheatSheet

#print(client.list_database_names())

#print(db.list_collection_names())

db = "CheatSheet"

print("This would create first object of CCMP class")

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
ccmpCode2.getall()
print("------------------------------------------------------------------")


#miConexion = Conn("CheatSheet","123")
#miConexion.closeConexion()






