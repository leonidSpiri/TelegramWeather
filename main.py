from api_requests import request


def print_hi(name):
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    data = request.get_weather("Moscow")
    text = 'Погода в Moscow \nТемпература: {0} C\nОщущается как: {1} C \nСкорость ветра: {2} м/с \n'.format(
        str(data["temp"]), str(data["feels_like"]), str(data["wind_speed"]))

    print(text)