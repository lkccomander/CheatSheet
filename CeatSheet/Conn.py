
from pymongo import MongoClient
from UtilService import UtilService
import pymongo
import UtilService
from bson import BSON
from bson import json_util
import json
import random
import code
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


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
        json_docs = []
        single_doc = mycol.find().sort("code", -1)
        new_dict = mycol.find().sort("code", -1)
        
        #for x in single_doc:
            #print(x)
        print("-------------------------------KAROL La Niña de las flores-5--------------------------------")

       
        #https://stackoverflow.com/questions/19674311/json-serializing-mongodb

        for doc in new_dict:
            json_doc = json.dumps(doc, default=json_util.default)
            #json_doc = json_doc.replace("$oid", "id")            #json_doc = json_doc.replace("_id", "uid")
            #print("---------------------------------------------------------------")
            #print(doc)
            json_docs.append(json_doc)
        
            
        print(json_docs)


        with open('data1.json', 'w') as outfile:
          json.dump(json_docs, outfile, sort_keys = True, indent = 4,ensure_ascii = False)
        
        # Write JSON file
        with io.open('data.json', 'w', encoding='utf8') as outfile:
          str_ = json.dumps(json_docs,indent=4, sort_keys=True,separators=(',', ': '), ensure_ascii=False)
          outfile.write(to_unicode(str_))
        #Check https://github.com/MartinThoma/mpu
        


        print("-------------------------------KAROL La Niña de las flores-6--------------------------------")
        #json_doc = json.dumps(single_doc,default=json_util.default)
        #json_doc = json_doc.replace("$oid", "id")
        #json_doc = json_doc.replace("_id", "uid")
        print("-------------------------------KAROL La Niña de las flores-7--------------------------------")
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



 







