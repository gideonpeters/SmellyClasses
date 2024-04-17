import json

class CookiesUtil:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cookies = {}

    def get_cookies(self, response):
        if 'cookies' in response:
            self.cookies = response['cookies']

    def load_cookies(self):
        try:
            with open(self.file_path, 'r') as file:
                self.cookies = json.load(file)
        except FileNotFoundError:
            self.cookies = {}
        return self.cookies

    def save_cookies(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.cookies, file)
            return True
        except Exception as e:
            print(f"Error saving cookies: {e}")
            return False

    def set_cookies(self, request):
        request['cookies'] = f"cookies={str(self.cookies)}"

if __name__ == '__main__':
    import unittest
    unittest.main()