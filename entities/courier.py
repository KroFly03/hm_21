class Courier:
    def __init__(self, request, storages):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.destination in storages:
            self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove(self.__request.item, self.__request.amount)
        print(f'Курьер забрал {self.__request.amount} {self.__request.item} из {self.__request.departure}')
        self.__to.add(self.__request.item, self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.item} в {self.__request.destination}')

    def cancel(self):
        self.__from.add(self.__request.item, self.__request.amount)
