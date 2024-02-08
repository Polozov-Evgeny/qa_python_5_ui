import random


class TestData:

    REGISTRATION_DATA = {'name': 'BurgerMan',
                         'email': 'evgenii_polozov_5_' + str(random.randint(100, 999)) + '@ya.ru',
                         'password': 'Zxc12345!'}

    LOGIN_DATA = {'email': 'evgenii_polozov_5@ya.ru',
                  'password': 'Zxc12345!'}
