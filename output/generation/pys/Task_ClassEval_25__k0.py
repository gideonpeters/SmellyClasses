import json

class CookiesUtil:
    """
    This is a class as utility for managing and manipulating Cookies, including methods for retrieving, saving, and setting Cookies data.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = None

    def get_cookies(self, response):
        """
        Gets the cookies from the specified response, and save it to cookies_file.
        :param response: The response to get cookies from, dict.
        """
        if 'cookies' in response:
            self.cookies = response['cookies']
            self._save_cookies()

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        """
        with open(self.cookies_file, 'r') as file:
            self.cookies = json.load(file)
        return self.cookies

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        with open(self.cookies_file, 'w') as file:
            json.dump(self.cookies, file)
        return True

    def set_cookies(self, request):
        """
        Sets the cookies from the class instance to the request dictionary.
        :param request: The request dictionary to set cookies in.
        """
        request['cookies'] = self.cookies
