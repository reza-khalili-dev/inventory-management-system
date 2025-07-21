#--------------------------database.py
import json


class File_manager:
    def __init__(self,file_path):
        self.file_path = f"data/{file_path}"
    
    def load(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save(self, data):
            try:
                with open(self.file_path, "w") as f:
                    json.dump(data, f, indent=4)
            except FileNotFoundError:
                print("ERROR: The 'data' directory does not exist! Please create it first.")
            except Exception as e:
                print("ERROR!!!", e)
                
                
            
