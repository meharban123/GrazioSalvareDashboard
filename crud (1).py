from pymongo import MongoClient
from pprint import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, inputUser, inputPass):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables

        #
        USER = inputUser
        PASS = inputPass
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30593
        DB = 'AAC'
        COL = 'animals'

        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            pprint(data)
            return True  # data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return False

    def read(self, query):
        if query is not None:
            cursor = self.database.animals.find(query)
            result = list(cursor)
            return result
        else:
            return [] ##empty list if nothing comes up
    def update(self, update_query, update_new):
        if update_query and update_new is not None:
            update_count = self.collection.update_one(update_query, {'$set': update_new})
            print("Number of documents updated:", update_count.modified_count)
            return update_count.modified_count ##will return count of modified
        return 0
##delete method
    def delete(self, delete_query):
        if delete_query is not None:
            delete_count = self.collection.delete_one(delete_query)
            print("Number of documents deleted:", delete_count.deleted_count)
            return delete_count.deleted_count ##will return count of delete
        return 0


    


    
