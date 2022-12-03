import requests

from ..settings import api_config


def get_place_coord(city):
    payload = {'geocode': city, 'apikey': api_config.geo_key, 'format': 'json'}
    r = requests.get('https://geocode-maps.yandex.ru/1.x', params=payload)
    geo = r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    return geo


def get_weather(city):
    coordinates = get_place_coord(city).split()
    payload = {'lat': coordinates[1], 'lon': coordinates[0], 'lang': 'ru_RU'}
    r = requests.get('https://api.weather.yandex.ru/v2/informers', params=payload, headers=api_config.weather_key)
    weather_data = r.json()
    return print(weather_data)
