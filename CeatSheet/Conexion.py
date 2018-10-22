#Python 3.6

from pymongo import MongoClient
import pymongo
import json
from bson import BSON
from bson import json_util
from CCMPcode import CCMPcode
import random
import code
import os
import configparser


from pymongo import MongoClient, DESCENDING
from pymongo.write_concern import WriteConcern
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo.read_concern import ReadConcern



config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

class Conexion():
    """description of class"""

db = ""



def __init__(self,pdb):
    print("This is the constructor method.") 
    self.db = pdb
    #self = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
    

        #db = client.CheatSheet

def openConexion(self):
    #try:
        self = pymongo.MongoClient("mongodb+srv://userMongo4:123admina@cluster0-0njxn.mongodb.net/test?retryWrites=true")
        #db = client.CheatSheet
    #except:
        #print ('Error on the Conexion')


#-------------------------#

def closeConexion(self):
        print ('Error on Closing')






 





