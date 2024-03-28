class Server:
    def __init__(self):
        self.white_list = []
        self.receive_struct = {}
        self.send_struct = {}

    def add_white_list(self, addr):
        if addr in self.white_list:
            return False
        self.white_list.append(addr)

    def del_white_list(self, addr):
        if addr not in self.white_list:
            return False
        self.white_list.remove(addr)

    def recv(self, info):
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return -1
        if info["addr"] not in self.white_list:
            return False
        self.receive_struct = info

    def send(self, info):
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return "info structure is not correct"
        self.send_struct = info

    def show(self, action):
        if action == "send":
            return self.send_struct if self.send_struct else False
        elif action == "receive":
            return self.receive_struct if self.receive_struct else False
        else:
            return False
