
from pymongo import MongoClient
import pymongo
import json
from bson import BSON
from bson import json_util
import random
import code


class Conn():
    """description of class"""
        
    db = ""
    port = ""

    def __init__(self, pdb, pport):
         print("This is the constructor method.")
         self.db = pdb
         self.port = pport
         self = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
    
    def setDB(self, pdb):
        self.db = pdb
    
    def getDB(self, pdb):
        self1 = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
        mydb = self1.CheatSheet
        mycol = mydb.CheatSheet
        single_doc = mycol.find().sort("name", -1)
        for x in single_doc:
            print(x)
        #json_doc = json.dumps(single_doc,default=json_util.default)
        #json_doc = json_doc.replace("$oid", "id")
        #json_doc = json_doc.replace("_id", "uid")
        #print(json_doc)
        #return json.loads(str(json_doc))
#-----------------------------------------------------------------------------------------------------------------------#
         
    def closeConexion(self):
          print ("Error on Closing")

    def getall(self):
           self = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
           print(self.list_database_names())

    def getallCollections(self,pdb):
           Client = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
           #db.list_collection_names()
           self.db = pdb



    def gettoo(self):
           self = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
           print(self.get_default_database())

    def get_all(self,table_name):
        conditions={}
        sort_index ='_id' 
        limit=100
        all_doc = self.db[table_name].find(conditions).sort(sort_index, pymongo.DESCENDING).limit(limit)
        json_doc = json.dumps(list(all_doc),default=json_util.default)
        json_doc = json_doc.replace("_id", "uid")
        return json.loads(str(json_doc))



 







