import os
import json

class BaseDataAccess:
    def __init__(self):
        pass

    #getting full path of db file
    current_dir = os.path.dirname(__file__) 
    rel_path = "../db.json"
    db_file_path = os.path.join(current_dir, rel_path)

    # Specifies which collection is using by class
    # Will override by each child classes
    collection_name = ""
    # Specifies what is the name of last given id property using by class
    # Will override by each child classes
    collection_id_field = ""

    #generic get all objects from specified collection of db by collection_name
    def get_all(self):
        #opens file with read permission
        file = open(self.db_file_path,"r")
        data = json.load(file)
        file.close()

        return data[self.collection_name]
    
    #generic add method to specified collection of db by collection_name
    def add(self, entity):
        file = open(self.db_file_path)
        data = json.load(file)

        #id incrementation is doing manually so the last given id storing in database with a specific object name 
        # name of last given id object stores in collection_id_field variable
        last_id = data[self.collection_id_field]
        # id of to be insert object is getting from db and setting to the object
        entity.id = last_id
        # the collection_id_field is incremented
        data[self.collection_id_field] = last_id + 1

        # the entity is appending to collection
        data[self.collection_name].append(entity.__dict__)
        #opens file with write permission
        file = open(self.db_file_path, "w")
        # manipulating json file
        json.dump(data, file)

            
    def delete(self, id):
        file = open(self.db_file_path)
        data  = json.load(file)
        
        # finds given id in db collection and delete it
        for item in data[self.collection_name]:
            if item["id"] == id:
                data[self.collection_name].remove(item)
                open(self.db_file_path, "w").write(json.dumps(data))
                return True
        
        # if the given id cannot find returns False
        return False

# Data Accessor Class for "contacts" collection
class ContactDataAccess(BaseDataAccess):
    def __init__(self):
        self.collection_name = "contacts"
        self.collection_id_field = "contactLastId"

