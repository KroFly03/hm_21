from entities.courier import Courier
from entities.request import Request
from entities.shop import Shop
from entities.store import Store
from exceptions import RequestError, CourierError

store = Store({
    'печенька': 25,
    'собачка': 25,
    'елка': 25,
    'пончик': 3,
    'зонт': 5,
    'ноутбук': 1,
})
shop = Shop({
    'печенька': 2,
    'собачка': 2,
    'елка': 2,
    'зонт': 1,
    'пончик': 1,
})

storages = {
    'магазин': shop,
    'склад': store,
}


while True:
    for storage in storages:
        print(f'В {storage}е хранится:\n{storages[storage].get_items()}')

    user_input = input(
        'Введите запроса в формате: <Доставить 3 собачка из склад в магазин>\n'
        'Введите <стоп/stop>, если хотите закончить\n'
    )

    if user_input in ['стоп', 'stop']:
        break

    try:
        request = Request(user_input, storages)
    except RequestError as ex:
        print(ex.message)
        continue

    courier = Courier(request, storages)

    try:
        courier.move()
    except CourierError as ex:
        print(ex.message)
        courier.cancel()
        continue
