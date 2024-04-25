class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def is_valid(self):
        octets = self.ip.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not octet.isdigit() or not 0 <= int(octet) <= 255:
                return False
        return True

    def get_octets(self):
        if not self.is_valid():
            return []
        return self.ip.split('.')

    def get_binary(self):
        if not self.is_valid():
            return ''
        binary_octets = []
        for octet in self.ip.split('.'):
            binary_octets.append(format(int(octet), '08b'))
        return '.'.join(binary_octets)
