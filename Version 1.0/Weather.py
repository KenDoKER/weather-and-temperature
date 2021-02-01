import PySimpleGUI as GUI #Интерфейс
import requests #Для получения данных с сайта
from bs4 import BeautifulSoup #Для обработки данных полученных с сайта

#Тема интерфейса
GUI.theme('DarkBrown1')

#Настройка Интерфейса
layout = [[GUI.Text('Погода в Казани сейчас:', font=('Helvetica', 20),  justification='center'), GUI.Text(size=(5, 3), font=('Helvetica', 20), key='-OUTPUT-')]]

#Ссылка на сайт
pageURL = "https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C"

window = GUI.Window('Weather', layout)

while True:                                 
    event, values = window.read(timeout=10) #Обновление данных в окне
    if event == GUI.WIN_CLOSED:
        break
    else:
    	req = requests.get(pageURL); soup = BeautifulSoup(req.content, 'html.parser'); weather = soup.find('div', {'class': 'weather__article_main_temp'}).text; window['-OUTPUT-'].update(weather) #Получение, Анализ, Поиск ивставка в интерфейс нужных данных
window.close()