import requests

from app.settings import API_KEY


def get_number():
    country_name = 'KZ'
    response_number = requests.get('http://simsms.org/priemnik.php?'
                                   'metod=get_number&'
                                   'country=' + country_name +
                                   '&'
                                   'service=opt41&'
                                   'apikey=' + API_KEY)
    json_response = response_number.json()
    if json_response['response'] == '2':
        country_name = 'RU'
        response_number = requests.get('http://simsms.org/priemnik.php?'
                                       'metod=get_number&'
                                       'country=' + country_name + '&'
                                       'service=opt41&'
                                       'apikey=' + API_KEY)
        json_response = response_number.json()
    if json_response['response'] == '1':
        phone_number = '+7' + json_response['number']
        print(phone_number)
        return phone_number