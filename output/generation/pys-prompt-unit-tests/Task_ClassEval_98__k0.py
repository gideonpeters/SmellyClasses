import xml.etree.ElementTree as ET
import os

class XMLProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.root = None

    def read_xml(self):
        tree = ET.parse(self.file_name)
        self.root = tree.getroot()
        return self.root

    def write_xml(self, output_file):
        tree = ET.ElementTree(self.root)
        tree.write(output_file)
        return os.path.exists(output_file)

    def process_xml_data(self, processed_file):
        for item in self.root.findall('item'):
            item.text = item.text.upper()
        tree = ET.ElementTree(self.root)
        tree.write(processed_file)
        return os.path.exists(processed_file)

    def find_element(self, element_name):
        return self.root.findall(element_name)
