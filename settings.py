import datetime

EMAIL = 'rick.flair@sushimadre.com'
PASSWORD = 'woooooooh'
DRIVER_PATH = "/path/to/chrome/chromedriver"


class Restaurant:
    def __init__(self, name, first_day):
        self.name = name
        self.first_day = first_day


SAUNDERS = Restaurant(
    "Sushi Madre - Saunders", datetime.datetime(2016, 12, 12)
)
MCPHERSON = Restaurant(
    "Sushi Madre - McPherson", datetime.datetime(2016, 12, 13)
)
LOOP20 = Restaurant(
    "Sushi Madre - Loop 20", datetime.datetime(2016, 12, 14)
)
DELMAR = Restaurant(
    "Sushi Madre - Del Mar", datetime.datetime(2017, 2, 22)
)
