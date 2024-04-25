class CamelCaseMap:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[self._convert_key(key)]

    def __setitem__(self, key, value):
        self.data[self._convert_key(key)] = value

    def __delitem__(self, key):
        del self.data[self._convert_key(key)]

    def __iter__(self):
        return iter(self.data.keys())

    def __len__(self):
        return len(self.data)

    def _convert_key(self, key):
        if isinstance(key, str):
            parts = key.split('_')
            return parts[0] + ''.join(word.capitalize() for word in parts[1:])
        return key

    @staticmethod
    def _to_camel_case(key):
        if isinstance(key, str):
            parts = key.split('_')
            return parts[0] + ''.join(word.capitalize() for word in parts[1:])
        return key