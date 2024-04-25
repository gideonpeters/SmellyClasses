class Hotel:
    def __init__(self, name, room_types):
        self.name = name
        self.room_types = room_types
        self.booked_rooms = {room_type: {} for room_type in room_types}
        self.available_rooms = {room_type: count for room_type, count in room_types.items()}

    def book_room(self, room_type, quantity, guest_name):
        if room_type not in self.room_types or quantity > self.available_rooms[room_type]:
            return False
        if guest_name in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][guest_name] += quantity
        else:
            self.booked_rooms[room_type][guest_name] = quantity
        self.available_rooms[room_type] -= quantity
        return 'Success!'

    def check_in(self, room_type, quantity, guest_name):
        if room_type not in self.room_types or quantity > self.available_rooms[room_type]:
            return False
        if guest_name in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][guest_name] -= quantity
            if self.booked_rooms[room_type][guest_name] == 0:
                del self.booked_rooms[room_type][guest_name]
            self.available_rooms[room_type] += quantity
        return True

    def check_out(self, room_type, quantity):
        if room_type not in self.room_types:
            return False
        self.available_rooms[room_type] += quantity
        return True

    def get_available_rooms(self, room_type):
        return self.available_rooms.get(room_type, 0)
