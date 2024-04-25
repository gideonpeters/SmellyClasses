import re

class RegexUtils:
    def match(self, pattern, text):
        return bool(re.match(pattern, text))

    def findall(self, pattern, text):
        return re.findall(pattern, text)

    def split(self, pattern, text):
        return re.split(pattern, text)

    def sub(self, pattern, replace, text):
        return re.sub(pattern, replace, text)

    def generate_email_pattern(self):
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def generate_phone_number_pattern(self):
        return r'\b\d{3}-\d{3}-\d{4}\b'

    def generate_split_sentences_pattern(self):
        return r'[.?!]\s+[A-Z]'

    def split_sentences(self, text):
        return re.split(r'[.?!]\s+', text)

    def validate_phone_number(self, phone_number):
        return bool(re.match(r'\b\d{3}-\d{3}-\d{4}\b', phone_number))

    def extract_email(self, text):
        return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
