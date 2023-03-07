import telebot
import settings



bot = telebot.TeleBot('6052649938:AAHRY1Ndy3wB378cidObLPspazWka1AEOW4')

@bot.message_handler(commands=['start'])
def start(message):
    button = telebot.types.KeyboardButton('/Расписание')
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add(button)
    bot.send_message(chat_id=message.chat.id, text='Привет, сливка!', reply_markup=keyboard)

@bot.message_handler(commands=['Расписание'])
def schedule(message):
    bot.send_message(chat_id=message.chat.id, text=f"Сегодня <b>{settings.weekday_name_russian}</b>", parse_mode="html")
    
    if not settings.schedule:
        bot.send_message(chat_id=message.chat.id, text='Ты бессмертн(-ый/-ая) что ли? Иди проспись')
        return

    message_text = "Расписание на сегодня:\n\n"

    for item in settings.schedule:
        if item.get('week_parity') is None:
            # message_text += '{}{}:\n'.format(item['time'], item['name'])
            message_text += f"{item['time']}{item['name']}:\n"

            for link in item["links"]:
                # message_text += '{}\n'.format(link)
                message_text += f"{link}\n"
        elif item.get('week_parity') is settings.week_parity:
            # message_text += '{}{}:\n'.format(item['time'], item['name'])
            message_text += f"{item['time']}{item['name']}:\n"

            for link in item["links"]:
                # message_text += '{}\n'.format(link)
                message_text += f"{link}\n"

    bot.send_message(chat_id=message.chat.id, text=message_text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
