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
        if self.root is not None:
            tree = ET.ElementTree(self.root)
            tree.write(output_file)
            return True
        return False

    def process_xml_data(self, output_file):
        if self.root is not None:
            for elem in self.root.iter():
                if elem.text is not None:
                    elem.text = elem.text.upper()
            tree = ET.ElementTree(self.root)
            tree.write(output_file)
            return True
        return False

    def find_element(self, element_name):
        elements = self.root.findall(element_name)
        return elements if elements else []

import unittest

class XMLProcessorTest(unittest.TestCase):
    def test_XMLProcessor(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n    <item>orange</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        root = self.processor.read_xml()
        self.assertIsNotNone(root)
        lst = root.findall('item')
        self.assertEqual(lst[0].text, 'apple')
        self.assertEqual(lst[1].text, 'banana')
        self.assertEqual(lst[2].text, 'orange')

        file_name = 'output.xml'
        result = self.processor.write_xml(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'apple')
        self.assertEqual(lst[1].text, 'banana')
        self.assertEqual(lst[2].text, 'orange')

        os.remove('output.xml')

        file_name = 'processed.xml'
        result = self.processor.process_xml_data(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'APPLE')
        self.assertEqual(lst[1].text, 'BANANA')
        self.assertEqual(lst[2].text, 'ORANGE')

        os.remove('processed.xml')

        element_name = 'item'
        root = self.processor.read_xml()
        elements = self.processor.find_element(element_name)
        self.assertEqual(len(elements), 3)
        self.assertEqual(elements[0].text, 'apple')
        self.assertEqual(elements[1].text, 'banana')
        self.assertEqual(elements[2].text, 'orange')

        os.remove('test.xml')