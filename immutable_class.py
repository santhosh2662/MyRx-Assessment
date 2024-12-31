class ImmutableClass:
    def __init__(self, name, id, date_of_joining, addresses):
        self._name = name
        self._id = id
        self._date_of_joining = date_of_joining
        self._addresses = tuple(addresses)

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def date_of_joining(self):
        return self._date_of_joining

    @property
    def addresses(self):
        return self._addresses

addresses = ["123 Elm St, Springfield", "456 Oak St, Metropolis"]
immutable = ImmutableClass("John Doe", "12345", "2020-01-01", addresses)
print(immutable.name, immutable.id, immutable.date_of_joining, immutable.addresses)
