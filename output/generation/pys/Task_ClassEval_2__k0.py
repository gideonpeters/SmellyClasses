class ArgumentParser:
    """
    This is a class for parsing command line arguments to a dictionary.
    """

    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args in a command line
        self.requried is a set that stores the required arguments
        self.types is a dict that stores type of every arguments.
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and invoke _convert_type to stores the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        """
        args = command_string.split()[1:]
        for arg in args:
            if '=' in arg:
                key, value = arg.split('=')
            else:
                key = arg
                value = True
            if key in self.types:
                value = self._convert_type(key, value)
            self.arguments[key] = value

        missing_args = self.required - set(self.arguments.keys())
        if missing_args:
            return False, missing_args
        return True, None

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        """
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        """
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        """
        if arg in self.types:
            if self.types[arg] == int:
                return int(value)
            elif self.types[arg] == bool:
                if value.lower() == 'true':
                    return True
                elif value.lower() == 'false':
                    return False
        return value
