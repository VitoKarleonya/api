import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Создание экземпляра класса UserAgent
ua = UserAgent()

# Генерация случайного User-Agent
random_user_agent = ua.random

# Указываем URL адрес сайта с погодой
url = 'https://www.gismeteo.ru'

# Отправляем GET запрос на сайт с указанием случайного User-Agent
response = requests.get(url, headers={'User-Agent': random_user_agent})

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Извлекаем название города
    city_name_tag = soup.find('title')
    if city_name_tag:
        city_name = city_name_tag.text.split(' - ')[0]
    else:
        city_name = 'Город не найден'

    # Ищем элементы с прогнозом температуры
    temperature_elements = soup.find_all(class_='unit_temperature_c')

    # Проверяем, что прогноз температуры найден
    if temperature_elements:
        # Извлекаем текст температуры и выводим его
        temperatures = [temp.text.strip() for temp in temperature_elements]
        print("Температурный прогноз для", city_name)
        for i, temp in enumerate(temperatures, start=1):
            print(f"Время {i}: {temp}°C")
    else:
        print("Прогноз температуры не найден на странице")
else:
    print("Ошибка при получении данных с сайта:", response.status_code)
