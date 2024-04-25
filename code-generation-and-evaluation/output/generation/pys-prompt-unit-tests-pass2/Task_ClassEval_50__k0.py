import os
import stat
import json

class JSONProcessor:
    def read_json(self, file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                return data
            except json.JSONDecodeError:
                return -1
        else:
            return 0

    def write_json(self, data, file_path):
        if not data or not file_path:
            return -1
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            return 1
        except PermissionError:
            return -1

    def process_json(self, file_path, remove_key):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                if remove_key in data:
                    del data[remove_key]
                with open(file_path, 'w') as file:
                    json.dump(data, file)
                return 1
            except json.JSONDecodeError:
                return -1
        else:
            return 0
