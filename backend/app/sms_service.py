import requests
import time

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
        response_id = json_response['id']
        return phone_number, country_name, response_id


def get_verification_code():
    country_name = get_number()[1].lower()
    response_id = get_number()[2]
    response_sms = requests.get('http://simsms.org/priemnik.php?'
                                'metod=get_sms'
                                '&country=' + country_name +
                                '&service=opt41'
                                '&id=' + str(response_id) +
                                '&apikey=' + API_KEY)
    json_response_sms = response_sms.json()
    while json_response_sms['response'] == '2':
        time.sleep(30)
        response_sms = requests.get('http://simsms.org/priemnik.php?'
                                    'metod=get_sms'
                                    '&country=' + country_name +
                                    '&service=opt41'
                                    '&id=' + str(response_id) +
                                    '&apikey=' + API_KEY)
    json_response_sms = response_sms.json()
    return json_response_sms['sms']
