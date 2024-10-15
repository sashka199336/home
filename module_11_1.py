class Requests:
  
    url = 'https://pikabu.ru/'

    response = requests.get(url)

    if response.status_code == 404:

        data = response.url
        print(f'Статус ответа: OK [код 404]')

    else:
        print('Ошибка при выполнении запроса')
