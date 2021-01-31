import PySimpleGUI as GUI
import geocoder
import requests
import webbrowser
from bs4 import BeautifulSoup

def now_T(): #Сегодня
    pageURL = "https://www.meteoservice.ru/weather/overview/" + g.city
    req = requests.get(pageURL) 
    soup = BeautifulSoup(req.content, 'html.parser')
    weather = soup.find('div', {'class': 'temperature margin-bottom-0'}).text
    weather = weather[1:]
    return weather

def next_T(): #На завтра
    pageURL = "https://www.meteoservice.ru/weather/tomorrow/" + g.city
    req = requests.get(pageURL) 
    soup = BeautifulSoup(req.content, 'html.parser')
    weather = soup.find('span', {'class': 'value'}).text
    weather = weather[0:]
    return weather

GUI.theme('DarkBrown1')

layout =   [[GUI.Text('Ваше местоположение:', text_color=('orange'), justification='center'), GUI.Text(size=(6, -1), text_color=('orange'), key='-OUTPUT-1')],
           [GUI.Text('Температура в вашем городе сегодня:', text_color=('orange'), justification='center'), GUI.Text(size=(5, 1), text_color=('orange'), key='-OUTPUT-2')],
           [GUI.Text('Температура в вашем городе на завтра:', text_color=('orange'), justification='center'), GUI.Text(size=(5, -1), text_color=('orange'), key='-OUTPUT-3')],
           [GUI.CloseButton('Завершить', button_color=('black', 'orange')), GUI.Text('                                        '), GUI.Button('Автор', button_color=('black', 'orange'))]]
window = GUI.Window('Погода', layout, no_titlebar=True, alpha_channel=.9, grab_anywhere=True)

g = geocoder.ip('me') #Местоположение
city = g.city #Город

while True:                                 
    event, values = window.read(timeout=5000) #Обновление данных в окне
    if event == GUI.WIN_CLOSED:
        break #Закрытие окна
    if event == 'Автор': #Окно с сылками на автора
        GUI.theme('DarkBrown1')
        layout_2 = [[GUI.Text("Автор: Исламов Амир", text_color=('orange'), )],
                   [GUI.Button('ВК', size=(7, 1), button_color=('black', 'orange')), GUI.Button('GitHub', size=(7, 1), button_color=('black', 'orange')), GUI.CloseButton('Выйти', button_color=('black', 'orange'))]]
        window_2 = GUI.Window('Погода', layout_2, no_titlebar=True, alpha_channel=.9, grab_anywhere=True)
        event_2, values_2 = window_2.read()
        if event_2 == 'ВК':
            webbrowser.open("https://vk.com/a8287")
        if event_2 == 'GitHub':
            webbrowser.open("https://github.com/KenDoKER")
    else:
        t_1 = now_T()
        t_2 = next_T()
        window['-OUTPUT-1'].update(city) #Вывод "Город"
        window['-OUTPUT-2'].update(t_1) #Вывод "Температура сегодня"
        window['-OUTPUT-3'].update(t_2) #Вывод "Температура на завтра"
window.close()