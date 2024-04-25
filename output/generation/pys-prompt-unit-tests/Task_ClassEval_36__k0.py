import datetime

class EmailClient:
    def __init__(self, email, capacity):
        self.email = email
        self.capacity = capacity
        self.inbox = []

    def send_to(self, receiver, content, size):
        if receiver.get_occupied_size() + size <= receiver.capacity:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            email_data = {
                "sender": self.email,
                "receiver": receiver.email,
                "content": content,
                "size": size,
                "time": timestamp,
                "state": 'unread'
            }
            receiver.inbox.append(email_data)
            return True
        return False

    def fetch(self):
        if self.inbox:
            email = self.inbox.pop(0)
            email['state'] = 'read'
            return email
        return None

    def is_full_with_one_more_email(self, size):
        return self.get_occupied_size() + size > self.capacity

    def get_occupied_size(self):
        return sum(email['size'] for email in self.inbox)

    def clear_inbox(self, size):
        new_inbox = []
        remaining_size = size
        for email in self.inbox:
            if email['size'] <= remaining_size:
                remaining_size -= email['size']
            else:
                new_inbox.append({'size': email['size'] - remaining_size})
                remaining_size = 0
        self.inbox = new_inbox

import unittest

class EmailClientTestSendTo(unittest.TestCase):
    # Unit tests for send_to method

class EmailClientTestFetch(unittest.TestCase):
    # Unit tests for fetch method

class EmailClientTestIsFullWithOneMoreEmail(unittest.TestCase):
    # Unit tests for is_full_with_one_more_email method

class EmailClientTestGetOccupiedSize(unittest.TestCase):
    # Unit tests for get_occupied_size method

class EmailClientTestClearInbox(unittest.TestCase):
    # Unit tests for clear_inbox method

class EmailClientTestMain(unittest.TestCase):
    # Main unit tests for the EmailClient class
`