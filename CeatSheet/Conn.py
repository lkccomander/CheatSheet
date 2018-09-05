
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
             
    def closeConexion(self):
          print ("Error on Closing")

    def getall(self):
           self = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
           print(self.list_database_names())

    def gettoo(self):
           self = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
           print(self.get_default_database())


 







