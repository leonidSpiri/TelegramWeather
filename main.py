import api_requests.request as api_request


def print_hi(name):
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    api_request.get_weather('Ленинградская область, Симагино, СНТ Надежда')
