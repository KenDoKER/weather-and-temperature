import requests #Для закачки Данных с сайта
import PySimpleGUI as GUI # Интерфейс
from bs4 import BeautifulSoup #Для анализа данных
import time

starttime = time.time() #Для создания зацикливания

GUI.theme('DarkAmber') #Тема интерфейса

#1 и 2 окно интерфейса
layout = [[GUI.Text('Обновить температуру в Казани на данный момент?')],            
                 [GUI.Submit("    Да    "),]]      
window = GUI.Window('Weather', layout)

#Ссылка на сайт
pageURL = "https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C"

#Скрипт
while True:
    time.sleep(0.1 - ((time.time() - starttime) % 0.1)) # Зацикливание времени
    req = requests.get(pageURL) #Получение Данных
    soup = BeautifulSoup(req.content, 'html.parser') #Прогон документа через Beautiful Soup
    event, values = window.read() 
    if event == GUI.WIN_CLOSED or event == 'Exit': #Выход
        break
    weather = soup.find('div', {'class': 'weather__article_main_temp'}).text #Поиск нужной информации
    GUI.popup('Погода в Казани сейчас', weather) #Вывод во 2 окно интерфейса