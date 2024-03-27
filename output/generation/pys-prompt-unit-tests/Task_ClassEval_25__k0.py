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

    def _save_cookies(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.cookies, file)
            return True
        except:
            return False

    def set_cookies(self, request):
        request['cookies'] = f"cookies={str(self.cookies)}"

if __name__ == '__main__':
    unittest.main()
```
This code defines the class `CookiesUtil` with methods to get cookies from a response, load cookies from a file, save cookies to a file, and set cookies in a request. It also includes the necessary import statements and the `if __name__ == '__main__':` block for running unit tes