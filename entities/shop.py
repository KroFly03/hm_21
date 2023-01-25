from entities.base_storage import BaseStorage
from exceptions import TooManyDifferentItems


class Shop(BaseStorage):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5 and name not in self.get_items():
            raise TooManyDifferentItems

        super().add(name, amount)
