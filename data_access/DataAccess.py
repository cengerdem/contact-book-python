import os
import json
from typing import ForwardRef

class BaseDataAccess:
    def __init__(self):
        pass

    current_dir = os.path.dirname(__file__) 
    rel_path = "../db.json"
    db_file_path = os.path.join(current_dir, rel_path)

    collection_name = ""
    collection_id_field = ""

    def get_all(self):
        file = open(self.db_file_path,"r")
        data = json.load(file)
        file.close()

        return data[self.collection_name]
    
    def add(self, entity):
        file = open(self.db_file_path)
        data = json.load(file)

        last_id = data[self.collection_id_field]
        entity.id = last_id
        data[self.collection_id_field] = last_id + 1

        data[self.collection_name].append(entity.__dict__)
        file = open(self.db_file_path, "w")
        json.dump(data, file)

            
    def delete(self, id):
        file = open(self.db_file_path)
        data  = json.load(file)
                                                  
        for item in data[self.collection_name]:
            if item["id"] == id:
                data[self.collection_name].remove(item)
                open(self.db_file_path, "w").write(
                json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
                )
                return True
        
        return False

class ContactDataAccess(BaseDataAccess):
    def __init__(self):
        self.collection_name = "contacts"
        self.collection_id_field = "contactLastId"

