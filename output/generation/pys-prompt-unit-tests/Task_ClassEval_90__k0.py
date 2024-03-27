class URLHandler:
    def __init__(self, url):
        self.url = url

    def get_scheme(self):
        if "://" in self.url:
            return self.url.split("://")[0]
        return None

    def get_host(self):
        if "://" in self.url:
            temp = self.url.split("://")[1]
            if "/" in temp:
                return temp.split("/")[0]
            return temp
        return None

    def get_path(self):
        if "://" in self.url:
            temp = self.url.split("://")[1]
            if "/" in temp:
                path = temp.split("/", 1)[1]
                return "/" + path
        return None

    def get_query_params(self):
        if "?" in self.url:
            query_string = self.url.split("?")[1]
            if "#" in query_string:
                query_string = query_string.split("#")[0]
            params = query_string.split("&")
            query_params = {}
            for param in params:
                key, value = param.split("=")
                query_params[key] = value
            return query_params
        return {}

    def get_fragment(self):
        if "#" in self.url:
            return self.url.split("#")[1]
        return None
