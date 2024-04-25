class SignInSystem:
    def __init__(self):
        self.users = {}
        self.signed_in_users = set()

    def add_user(self, username):
        if username in self.users:
            return False
        self.users[username] = True
        return True

    def sign_in(self, username):
        if username in self.users:
            self.signed_in_users.add(username)
            return True
        return False

    def check_sign_in(self, username):
        return username in self.signed_in_users

    def all_signed_in(self):
        return len(self.signed_in_users) == len(self.users)

    def all_not_signed_in(self):
        return [user for user in self.users if user not in self.signed_in_users]
