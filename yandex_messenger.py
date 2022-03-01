from messenger import Messenger


class YandexMessenger(Messenger):
    url: str

    def __init__(self):
        Messenger.__init__(self, 'https://passport.yandex.ru/auth')

