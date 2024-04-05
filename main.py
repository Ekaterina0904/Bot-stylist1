import telebot
import os
import random
from dotenv import load_dotenv
load_dotenv()

TG_bot_pas = os.getenv('TG_token')


bot = telebot.TeleBot(TG_bot_pas)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')
    bot.send_message(message.chat.id, 'Ответьте на несколько вопросов и мы определим ваш цветотип: /go')
    bot.send_message(message.chat.id, 'Выбери свой цветотип: /winter, /spring, /summer, /autumn')
ids = [1402861894]

@bot.message_handler(func=lambda message: message.text == 'Дай мне мой id')
def start(message):
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    bot.send_message(message.chat.id, message.from_user.id)



@bot.message_handler(commands=['winter'])
def send_a_dog(message):
    print('Зима -> ', message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    dogs_folder_path = './Цветотип зима/'
    files = os.listdir(dogs_folder_path)
    rnd_dog_from_folder = random.choice(files)

    bot.send_photo(message.chat.id, open(dogs_folder_path + rnd_dog_from_folder, 'rb'))
    bot.send_message(message.chat.id, 'Обладателям цветотипа «Зима» подходят глубокие цвета в одежде с холодным подтоном, среди них темный синий, черный, серый, бордовый. Из светлых можно выбрать белый, розовый с холодным подтоном.')

@bot.message_handler(commands=['summer'])
def send_a_dog(message):
    print('Лето -> ', message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    dogs_folder_path = './цветотип лето/'
    files = os.listdir(dogs_folder_path)
    rnd_dog_from_folder = random.choice(files)

    bot.send_photo(message.chat.id, open(dogs_folder_path + rnd_dog_from_folder, 'rb'))
    bot.send_message(message.chat.id, 'ЛЕТО - это цветотип: по глубине - светлый, по насыщенности - мягкий, по подтону - холодный.\
                                       Для него характерны русые волосы с холодным оттенком, светлые глаза, светлая кожа с холодным подтоном.')

@bot.message_handler(commands=['autumn'])
def send_a_dog(message):
    print('Осень -> ', message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    dogs_folder_path = './цветотип осень/'
    files = os.listdir(dogs_folder_path)
    rnd_dog_from_folder = random.choice(files)

    bot.send_photo(message.chat.id, open(dogs_folder_path + rnd_dog_from_folder, 'rb'))
    bot.send_message(message.chat.id, 'Для «осеннего» типа внешности характерна персиковая либо светлая кожа с теплым подтоном. Цвет волос обычно рыже-русый или каштановый с медным отливом. Глаза насыщенного оттенка: зеленые, ярко-голубые или светло-карие.')

@bot.message_handler(commands=['spring'])
def send_a_dog(message):
    print('Весна -> ', message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    dogs_folder_path = './цветотип весна/'
    files = os.listdir(dogs_folder_path)
    rnd_dog_from_folder = random.choice(files)

    bot.send_photo(message.chat.id, open(dogs_folder_path + rnd_dog_from_folder, 'rb'))
    bot.send_message(message.chat.id, 'Это солнечный колорит, который привлекает теплой палитрой. Вот, чем выделяется представитель этого типажа:цвет волос — чаще всего русый, соломенный, льняной;\
                                          брови — светлые, в тон волос;\
                                          кожа — персиковая, бежевая или оттенка слоновой кости;\
                                          глаза — нежно-голубые, зеленые, ореховые;')

@bot.message_handler(commands = ['go'])
def test(message):
    bot.send_message(message.chat.id, 'К какому оттенку ближе ваш естественный цвет волос?')
    bot.send_message(message.chat.id, '/a) От темно-коричневых до иссиня-черных. ')
    bot.send_message(message.chat.id, '/b) Натуральный цвет волос преимущественно теплых оттенков блонда и светло-русые — пшеничные, медовые, золотистые, светло-каштановые')
    bot.send_message(message.chat.id, '/c) Темно-русый, светло-русый, иногда темно-коричневый')
    bot.send_message(message.chat.id, '/d) Цвет меди от золотистых до ярко-рыжих и даже красных')

@bot.message_handler(commands=['d'])
def send_a_dog(message):
    print('Осень -> ', message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    dogs_folder_path = './цветотип осень/'
    files = os.listdir(dogs_folder_path)
    rnd_dog_from_folder = random.choice(files)

    bot.send_photo(message.chat.id, open(dogs_folder_path + rnd_dog_from_folder, 'rb'))
    bot.send_message(message.chat.id, 'Для «осеннего» типа внешности характерна персиковая либо светлая кожа с теплым подтоном. Цвет волос обычно рыже-русый или каштановый с медным отливом. Глаза насыщенного оттенка: зеленые, ярко-голубые или светло-карие.')

@bot.message_handler(commands=['c'])
def send_a_dog(message):
    print('Весна -> ', message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    dogs_folder_path = './цветотип весна/'
    files = os.listdir(dogs_folder_path)
    rnd_dog_from_folder = random.choice(files)

    bot.send_photo(message.chat.id, open(dogs_folder_path + rnd_dog_from_folder, 'rb'))
    bot.send_message(message.chat.id, 'Это солнечный колорит, который привлекает теплой палитрой. Вот, чем выделяется представитель этого типажа:цвет волос — чаще всего русый, соломенный, льняной;\
                                          брови — светлые, в тон волос;\
                                          кожа — персиковая, бежевая или оттенка слоновой кости;\
                                          глаза — нежно-голубые, зеленые, ореховые;')

    @bot.message_handler(commands=['b'])
    def send_a_dog(message):
        print('Лето -> ', message.from_user.first_name, message.from_user.last_name, message.from_user.username)
        dogs_folder_path = './цветотип лето/'
        files = os.listdir(dogs_folder_path)
        rnd_dog_from_folder = random.choice(files)

        bot.send_photo(message.chat.id, open(dogs_folder_path + rnd_dog_from_folder, 'rb'))
        bot.send_message(message.chat.id, 'ЛЕТО - это цветотип: по глубине - светлый, по насыщенности - мягкий, по подтону - холодный.\
                                           Для него характерны русые волосы с холодным оттенком, светлые глаза, светлая кожа с холодным подтоном.')


@bot.message_handler(commands=['a'])
def send_a_dog(message):
    print('Зима -> ', message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    dogs_folder_path = './Цветотип зима/'
    files = os.listdir(dogs_folder_path)
    rnd_dog_from_folder = random.choice(files)

    bot.send_photo(message.chat.id, open(dogs_folder_path + rnd_dog_from_folder, 'rb'))
    bot.send_message(message.chat.id, 'Обладателям цветотипа «Зима» подходят глубокие цвета в одежде с холодным подтоном, среди них темный синий, черный, серый, бордовый. Из светлых можно выбрать белый, розовый с холодным подтоном.')


@bot.message_handler(func=lambda message: message.from_user.id in ids)
def creator(message):
    bot.send_message(message.chat.id, 'Здраствуй, Создатель!')
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAMgZNQIduhA5xXEnxdk2XhVlKmOGzUAAjMAA845CA3luMcN7o5ENTAE')








bot.infinity_polling()