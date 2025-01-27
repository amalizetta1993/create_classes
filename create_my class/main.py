import datetime

class YandexStation:
    def __init__(self, type_station, display, status, location):
        self.type_station = type_station
        self.display = display
        self.status = status
        self.location = location
        
    #функция получения данных
    def get_data(self):
        return self.type  
    
    # #функция включения/выключения Алисы 
    def set_status(self, change_status):
        self.status = change_status
        if self.status =='On':
            new_status = 'Алиса включена'
        else:
            new_status = 'Алиса выключена'
        return new_status
                     
    # #функция приветствия Алисы  
    def get_alice_greeting(self, user_name):
        self.user_name = user_name
        if self.status == 'On':
            if self.display == True:
                greeting = f'Привет, {self.user_name}! Я твой новый помощник Алиса {self.type_station}! С моей помощью ты можешь смотреть фильмы и видео'
            else:
                greeting = f'Привет, {self.user_name}! Я твой новый помощник Алиса {self.type_station}! С моей помощью ты можешь слушать музыку и узнавать погоду'
        else:
            greeting = ''    
        return greeting

    #функция советов в зависимости от локации
    def get_advice_scenarious(self, user_name, user_age):
        self.user_age = user_age
        self.user_name = user_name        
        if self.status == 'On':
            if self.user_age > 10:
                if self.location == 'Детская':
                    scenarious = f'Привет, {self.user_name}! Вы можете включить радионяню'
                elif self.location == 'Кухня':
                    scenarious = f'Привет, {self.user_name}! Я могу рассказать вам новый рецепт'   
                elif self.location == 'Спальня':
                    scenarious = f'Привет, {self.user_name}! Вы можете включить музыку для сна'   
                elif self.location == 'Спортзал':
                    scenarious = f'Привет, {self.user_name}! Вы можете включить бодрую музыку для тренировок'               
            else:
                scenarious = f'Привет, {self.user_name}! Я твой новый друг! В любое время я могу рассказать тебе сказку'
        else:
            scenarious = ''    
        return scenarious   
    
    #функция будильник
    def set_alarm_clock(self, time):
        if self.status == 'On':
            self.time = time
            alarm = f'Ваш будильник установлен на {self.time}'
        else:
            alarm = ''
        return alarm

yandex_station1 = YandexStation('Мини', False, 'On', 'Детская')
yandex_station2 = YandexStation('Дуо Макс', True, 'On', 'Кухня')
yandex_station3 = YandexStation('Макс ТВ', True, 'Off', 'Спальня')
yandex_station4 = YandexStation('Миди', False, 'On', 'Спортзал')


user_name = input('Введите ваше имя: ')
user_age = int(input('Введите ваш возраст: '))

#Алиса нас приветствует
print(yandex_station1.get_alice_greeting(user_name))
print(yandex_station2.get_alice_greeting(user_name))
print(yandex_station3.get_alice_greeting(user_name))
print(yandex_station4.get_alice_greeting(user_name))

#Включаем/выключаем Алису
print(yandex_station1.set_status('On'))
print(yandex_station2.set_status('Off'))
print(yandex_station3.set_status('On'))
print(yandex_station4.set_status('Off'))

#Предлагаем пользователю сценарий
print(yandex_station1.get_advice_scenarious(user_name, user_age))
print(yandex_station2.get_advice_scenarious(user_name, user_age))
print(yandex_station3.get_advice_scenarious(user_name, user_age))
print(yandex_station4.get_advice_scenarious(user_name, user_age))

#Устанавливаем будильник
print(yandex_station1.set_alarm_clock('7:00'))
print(yandex_station2.set_alarm_clock('10:00'))
print(yandex_station3.set_alarm_clock('15:00'))
print(yandex_station4.set_alarm_clock('20:00'))