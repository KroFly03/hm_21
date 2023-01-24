from exceptions import InvalidRequest, InvalidStorageName


class Request:
    def __init__(self, info, storages):
        splitted_info = info.lower().split(' ')

        if len(splitted_info) != 7:
            raise InvalidRequest

        self.amount = int(splitted_info[1])
        self.item = splitted_info[2]
        self.departure = splitted_info[4]
        self.destination = splitted_info[6]

        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName
