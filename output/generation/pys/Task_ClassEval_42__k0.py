class Hotel:
    def __init__(self, name, room_types):
        self.name = name
        self.available_rooms = room_types.copy()
        self.booked_rooms = {}

    def book_room(self, room_type, quantity, guest_name):
        if room_type not in self.available_rooms:
            return False
        if self.available_rooms[room_type] < quantity:
            return quantity - self.available_rooms[room_type]
        self.available_rooms[room_type] -= quantity
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        if guest_name not in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][guest_name] = quantity
        else:
            self.booked_rooms[room_type][guest_name] += quantity
        return 'Success!'

    def check_in(self, room_type, quantity, guest_name):
        if room_type not in self.booked_rooms or guest_name not in self.booked_rooms[room_type]:
            return False
        if self.booked_rooms[room_type][guest_name] < quantity:
            return False
        self.booked_rooms[room_type][guest_name] -= quantity
        if self.booked_rooms[room_type][guest_name] == 0:
            del self.booked_rooms[room_type][guest_name]
        self.available_rooms[room_type] += quantity
        return True

    def check_out(self, room_type, quantity):
        if room_type not in self.booked_rooms:
            return
        for guest_name, booked_quantity in self.booked_rooms[room_type].items():
            if quantity <= 0:
                break
            if booked_quantity >= quantity:
                self.booked_rooms[room_type][guest_name] -= quantity
                if self.booked_rooms[room_type][guest_name] == 0:
                    del self.booked_rooms[room_type][guest_name]
                self.available_rooms[room_type] += quantity
                quantity = 0
            else:
                quantity -= booked_quantity
                self.available_rooms[room_type] += booked_quantity
                del self.booked_rooms[room_type][guest_name]

    def get_available_rooms(self, room_type):
        return self.available_rooms.get(room_type, 0)
