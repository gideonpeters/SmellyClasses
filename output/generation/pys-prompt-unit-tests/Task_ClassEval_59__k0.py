import datetime

class MovieBookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, seats):
        movie = {
            'name': name,
            'price': price,
            'start_time': datetime.datetime.strptime(start_time, '%H:%M'),
            'end_time': datetime.datetime.strptime(end_time, '%H:%M'),
            'seats': [[0 for _ in range(seats)] for _ in range(seats)]
        }
        self.movies.append(movie)

    def book_ticket(self, movie_name, seats_to_book):
        for movie in self.movies:
            if movie['name'].lower() == movie_name.lower():
                for seat in seats_to_book:
                    if movie['seats'][seat[0]][seat[1]] == 1:
                        return 'Booking failed.'
                    movie['seats'][seat[0]][seat[1]] = 1
                return 'Booking success.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        available = []
        current_time = datetime.datetime.strptime(start_time, '%H:%M')
        end_time = datetime.datetime.strptime(end_time, '%H:%M')
        for movie in self.movies:
            if movie['start_time'] <= current_time <= movie['end_time'] and movie['end_time'] <= end_time:
                available.append(movie['name'])
        return available
