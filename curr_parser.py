import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import matplotlib.pyplot as plt 
from datetime import datetime

ua = UserAgent()
random_user_agent = ua.random
url = 'https://mfd.ru/currency/?currency=USD'
req = requests.get(url, headers={'User-Agent': random_user_agent})
soup = BeautifulSoup(req.content, 'html.parser')
currency = soup.find('table', class_='mfd-table mfd-currency-table').find_all('td')
curr_list = []
for cur in currency:
    curr_list.append(cur.text)



data_list = []
value_list = []
change_list = []

for index,element in enumerate(curr_list):
    if index %3 == 0:
        date_str = element.replace('с ', '')
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        data_list.append(date_obj)

    elif index %3 == 1:
        value_list.append(float(element.replace(',', '.')))
    elif index %3 == 2:
        change_list.append(float(element.replace('−', '-').replace(',', '.')))
	



plt.plot(data_list, value_list)

# Добавление заголовка и подписей к осям
plt.title('Пример графика')
plt.xlabel('X-ось')
plt.ylabel('Y-ось')

# Отображение графика
plt.show()


