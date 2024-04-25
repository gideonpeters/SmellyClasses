class ArgumentParser:
    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def add_argument(self, arg_name, required=False, arg_type=str):
        if required:
            self.required.add(arg_name)
        self.types[arg_name] = arg_type

    def parse_arguments(self, command_str):
        args = command_str.split()[1:]
        for arg in args:
            if '=' in arg:
                key, value = arg.split('=')
            else:
                key = arg
                value = True
            if key.startswith('--'):
                key = key[2:]
            if key in self.types:
                self.arguments[key] = self._convert_type(key, value)
        missing_args = self.required - set(self.arguments.keys())
        result = not bool(missing_args)
        return result, missing_args if missing_args else None

    def get_argument(self, arg_name):
        return self.arguments.get(arg_name)

    def _convert_type(self, key, value):
        if key in self.types:
            if self.types[key] == int:
                return int(value)
            elif self.types[key] == bool:
                return value.lower() in ['true', 'yes', '1']
            else:
                return value

if __name__ == '__main__':
    unittest.main()
