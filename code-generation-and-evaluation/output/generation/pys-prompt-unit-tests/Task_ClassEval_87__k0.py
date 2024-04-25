import datetime

class TimeUtils:
    def __init__(self):
        self.datetime = datetime.datetime.now()

    def get_current_time(self):
        return self.datetime.strftime("%H:%M:%S")

    def get_current_date(self):
        return self.datetime.strftime("%Y-%m-%d")

    def add_seconds(self, seconds):
        return (self.datetime + datetime.timedelta(seconds=seconds)).strftime("%H:%M:%S")

    def string_to_datetime(self, string):
        return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')

    def datetime_to_string(self, dt):
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def get_minutes(self, start_time, end_time):
        start_dt = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end_dt = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        diff = end_dt - start_dt
        return int(diff.total_seconds() / 60)

    def get_format_time(self, year, month, day, hour, minute, second):
        return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
