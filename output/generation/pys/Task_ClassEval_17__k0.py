from datetime import datetime, timedelta

class CalendarUtil:
    """
    This is a class as CalendarUtil that provides functionalities to manage calendar events, schedule appointments, and perform conflict checks.
    """

    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.
        """
        self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        """
        if event in self.events:
            self.events.remove(event)

    def get_events(self, date):
        """
        Get all events on a given date.
        """
        return [event for event in self.events if event['date'] == date]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        """
        for event in self.events:
            if not (end_time <= event['start_time'] or start_time >= event['end_time']):
                return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        """
        available_slots = []
        start_time = datetime(date.year, date.month, date.day, 0, 0)
        end_time = datetime(date.year, date.month, date.day, 23, 59)
        for event in self.events:
            if event['date'] == date:
                if start_time < event['start_time']:
                    available_slots.append((start_time, event['start_time']))
                start_time = event['end_time']
        if start_time < end_time:
            available_slots.append((start_time, end_time))
        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from the current date.
        """
        current_date = datetime.now()
        upcoming_events = []
        for event in self.events:
            if event['date'] >= current_date:
                upcoming_events.append(event)
        return upcoming_events[:num_events]
