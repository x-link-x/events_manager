class Event():

    def __init__(self, name, num_of_guests, room, description, start_date):
        self.name = name
        self.num_of_guests = num_of_guests
        self.room = room
        self.description = description
        self.start_date = start_date
        self.recurring = False
         