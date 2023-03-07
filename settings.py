import datetime
import json


FIRST_WEEK_NUMBER = 10
today = datetime.date.today()

#Получаем название дня недели
weekday_name = today.strftime('%A').lower()
weekday_name_russian_dict = {
    "monday": "Понедельник",
    "tuesday": "Вторник",
    "wednesday": "Среда",
    "thursday": "Четверг",
    "friday": "Пятница",
    "saturday": "Суббота",
    "sunday": "Воскресенье"
}
weekday_name_russian = weekday_name_russian_dict.get(weekday_name, weekday_name)

#Узнаём номер недели
current_week_number = today.isocalendar()[1]

#Проверка на чётность/нечётность False - нечётная, True - чётная
week_parity = False
if (current_week_number - FIRST_WEEK_NUMBER) % 2 == 0:
    week_parity = False
else:
    week_parity = True

#Получаем расписание
with open('schedule.json', encoding='utf-8') as f:
    schedule = json.load(f).get(weekday_name)