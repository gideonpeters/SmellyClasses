from datetime import datetime

class CalendarUtil:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        self.events = [e for e in self.events if e != event]

    def get_events(self, date):
        return [e for e in self.events if e['date'] == date]

    def is_available(self, start_time, end_time):
        for event in self.events:
            if event['start_time'] < end_time and event['end_time'] > start_time:
                return False
        return True

    def get_available_slots(self, date):
        available_slots = []
        for i in range(24):
            start_time = datetime(date.year, date.month, date.day, i, 0)
            end_time = datetime(date.year, date.month, date.day, i+1, 0)
            if self.is_available(start_time, end_time):
                available_slots.append((start_time, end_time))
        return available_slots

    def get_upcoming_events(self, days):
        upcoming_events = []
        today = datetime.now()
        for event in self.events:
            if (event['date'] - today).days <= days:
                upcoming_events.append(event)
        return upcoming_events
