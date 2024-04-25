import os
import zipfile

class ZipFileProcessor:
    def __init__(self, zip_file_name):
        self.zip_file_name = zip_file_name

    def read_zip_file(self):
        zip_file = zipfile.ZipFile(self.zip_file_name, 'r')
        return zip_file

    def extract_all(self, output_directory):
        try:
            with zipfile.ZipFile(self.zip_file_name, 'r') as zip_file:
                zip_file.extractall(output_directory)
            return True
        except Exception as e:
            print(f"Error extracting zip file: {e}")
            return False

    def extract_file(self, file_name, output_directory):
        try:
            with zipfile.ZipFile(self.zip_file_name, 'r') as zip_file:
                zip_file.extract(file_name, output_directory)
            return True
        except Exception as e:
            print(f"Error extracting file from zip: {e}")
            return False

    def create_zip_file(self, files_to_zip, new_zip_file):
        try:
            with zipfile.ZipFile(new_zip_file, 'w') as zip_file:
                for file in files_to_zip:
                    zip_file.write(file, os.path.basename(file))
            return True
        except Exception as e:
            print(f"Error creating zip file: {e}")
            return False
