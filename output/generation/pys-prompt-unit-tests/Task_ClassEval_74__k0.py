class Server:
    def __init__(self):
        self.white_list = []
        self.receive_struct = {}
        self.send_struct = {}

    def add_white_list(self, addr):
        if addr not in self.white_list:
            self.white_list.append(addr)
            return True
        return False

    def del_white_list(self, addr):
        if addr in self.white_list:
            self.white_list.remove(addr)
            return True
        return False

    def recv(self, info):
        if isinstance(info, dict) and "addr" in info and "content" in info:
            if info["addr"] in self.white_list:
                self.receive_struct = info
                return True
            return False
        return -1

    def send(self, info):
        if isinstance(info, dict) and "addr" in info and "content" in info:
            self.send_struct = info
            return True
        return "info structure is not correct"

    def show(self, action):
        if action == "send":
            return self.send_struct if self.send_struct else False
        elif action == "receive":
            return self.receive_struct if self.receive_struct else False
        return False
