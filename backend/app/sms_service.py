import requests

from app.settings import API_KEY


def get_number():
    country_name = 'KZ'
    response_number = requests.get('http://simsms.org/priemnik.php?'
                                   'metod=get_number&'
                                   'country=' + country_name + '&'
                                                               'service=opt41&'
                                                               'apikey=' + API_KEY)
    return response_number
number = get_number()
print(number)