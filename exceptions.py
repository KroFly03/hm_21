class BaseError(Exception):
    message = 'Непридвиденная ошибка'


class RequestError(BaseError):
    message = 'Ошибка запроса'


class CourierError(BaseError):
    message = 'Ошибка оформления доставки'


class NotEnoughSpace(CourierError):
    message = 'Недостаточно места'


class NotExistItem(CourierError):
    message = 'Товара не существует'


class TooMuchAmount(CourierError):
    message = 'Слишком большое количество товара'


class TooManyDifferentItems(CourierError):
    message = 'Слишком много разных товаров'


class InvalidRequest(RequestError):
    message = 'Неправильный запрос'


class InvalidStorageName(RequestError):
    message = 'Неправильное название пункта отправки/доставки'
