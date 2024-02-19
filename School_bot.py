import telebot
import json
import requests

streets = []
docs = []

API_URL='https://7012.deeppavlov.ai/model'

def save_str():
    with open("streets.json","w",encoding="utf-8") as ss:
        ss.write(json.dumps(streets,ensure_ascii=False))
    print("Список улиц успешно сохранен в файле streets.json")

def load_str():
    global streets
    with open("streets.json","r",encoding="utf-8") as ss:
        streets=json.load(ss)
    print("Список улиц успешно загружен!")   

def save_docs():
    with open("docs.json","w",encoding="utf-8") as sd:
        sd.write(json.dumps(docs,ensure_ascii=False))
    print("Список документов успешно сохранен в файле docs.json")

def load_docs():
    global docs
    with open("docs.json","r",encoding="utf-8") as sd:
        docs=json.load(sd)
    print("Список документов успешно загружен!")   


API_TOKEN=''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])

def start_message(message):
    try:
        load_str()
        bot.send_message(message.chat.id,"Список улиц успешно загружен!")

    except:
        streets.append("пер. Глинки")
        streets.append("пер. Краснокубанский")
        streets.append("пер. Пионерский")
        streets.append("пер. Почтовый")
        streets.append("ул. Железнодорожная")
        streets.append("ул. Базарная")
        streets.append("ул. Водопроводная")
        streets.append("ул. Гагарина")
        streets.append("ул. Калинина")
        streets.append("ул. Фрунзе")
        streets.append("ул. Энгельса")
        streets.append("ул. Революционная")
        bot.send_message(message.chat.id,"Список улиц загружен по умолчанию!")

    try:
        load_docs()
        bot.send_message(message.chat.id,"Список документов успешно загружен!")

    except:
        docs.append("Паспорт родителя")
        docs.append("Свидетельство о рождении ребёнка")
        docs.append("Сведения о регистрации")
        docs.append("Информация о братьях и сёстрах, если они уже учатся в нашей школе")
        docs.append("Документы, подтверждающие право на льготы")
        bot.send_message(message.chat.id,"Список документов загружен по умолчанию!")
    
    bot.send_message(message.chat.id,"Здравствуйте!\nЯ школо-бот от МБОУ СОШ №1 г. Невинномысска!\nЯ отвечаю на вопросы, связанные с приемом ребенка в школу.")

@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id,"Список улиц, закрепленных за школой №1")
    bot.send_message(message.chat.id, ", ".join(streets))
    bot.send_message(message.chat.id,"Перечень документов для приема в школу")
    bot.send_message(message.chat.id, ", ".join(docs))

@bot.message_handler(commands=['ss'])
def save_str(message):
    with open("streets.json","w",encoding="utf-8") as ss:
        ss.write(json.dumps(streets,ensure_ascii=False))
    print("Список улиц успешно сохранен в файле streets.json")

@bot.message_handler(commands=['sd'])
def save_docs(message):
    with open("docs.json","w",encoding="utf-8") as sd:
        sd.write(json.dumps(docs,ensure_ascii=False))
    print("Список документов успешно сохранен в файле docs.json")


@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq=" ".join(quest)
    data = { 'question_raw': [qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Попробуйте еще раз: /wiki Ваш запрос")

bot.polling()