class Worker:
    def __init__(self, name, id, address, phone_number, email):
        self.name = name
        self.id = id
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return "{},{},{},{},{}".format(self.name, self.id, self.address,
                                       self.phone_number, self.email)

    def __lt__(self, other):
        if isinstance(other, Worker):
            return self.id < other.id

    def __gt__(self, other):
        if isinstance(other, Worker):
            return self.id > other.id

    def __le__(self, other):
        if isinstance(other, Worker):
            return self.id <= other.id

    def __ge__(self, other):
        if isinstance(other, Worker):
            return self.id >= other.id

    def __eq__(self, other):
        if isinstance(other, Worker):
            return self.id == other.id


class MissingDataException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{} is missing.".format(self.value)


class EmailFormatException(Exception):
    pass


class PhoneNumberException(Exception):
    pass
