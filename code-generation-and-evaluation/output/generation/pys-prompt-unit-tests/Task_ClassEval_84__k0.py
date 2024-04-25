import json
import os
from unittest.mock import MagicMock

class TextFileProcessor:
    def __init__(self, file):
        self.file = file

    def read_file_as_json(self):
        with open(self.file, 'r') as f:
            data = json.load(f)
        return data

    def read_file(self):
        with open(self.file, 'r') as f:
            data = f.read()
        return data

    def write_file(self, content):
        with open(self.file, 'w') as f:
            f.write(content)

    def process_file(self):
        content = self.read_file()
        processed_content = ''.join(filter(str.isalnum, content))
        self.write_file(processed_content)
        return processed_content
`