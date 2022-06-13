from vkbottle import *
from vkbottle.bot import *
import src.creater_qr_code as qr
import src.creater_sign as sg
import os
import random
import time

# вводим переменную, которая немного упростит жизнь, используем ее в async функции nft
DIR = 'img/nft'
# вводим путь к картинке с погодой
WTIMG = 'img/weather.png'

# вводи токен группы, предворительно включив лонгпулл и все разрешения для бота
bot = Bot("ВАШ ТОКЕН ГРУППЫ ВК")
photo_uploader = PhotoMessageUploader(
    bot.api, generate_attachment_strings=True)


# функция запускающая в фоновом режиме генерацию картинки с информацией о погоде
# необоходимо написать полный путь до weather_update.pyw
# файл должен быть с расширением .pyw чтобы он запусклся на фоне
def weather():
    os.startfile(
        "ВАШ ПОЛНЫЙ ПУТЬ ДО weather_updater.pyw")


# принимаем сообщение !pogoda и отправляем результат
@bot.on.message(text='!pogoda')
async def pogoda(ans: Message):
    # вызываем функцию генерации погоды
    weather()
    i = False
    # проверка на наличие картинки с информацией о погоде
    while i == False:
        if os.path.isfile(WTIMG) == True:
            # прекрощаем цикл
            i = True
            # отправляем картинку на сервер и отправляем сообщение
            img = await photo_uploader.upload('img/weather.png')
            await ans.answer('погода в Тюмени сейчас:', attachment=img)
            continue
    # проверяем на наличие этого файла и удаляем его,
    # чтобы в следующий раз проверка, которая сверху, сработала нормально
    # иначе код сверху бы скинул старый файл
    if os.path.isfile(WTIMG) == True:
        os.remove(WTIMG)


# принимаем сообщение !sign и значение, отправляем результат
@bot.on.message(text='!sign <name>')
async def sign(ans: Message, name):
    # вызываем функцию из другого файла
    sg.create_sign(name)
    # отправляем картинку на сервер и отправляем сообщение
    img = await photo_uploader.upload('img/sign.png')
    await ans.answer('ваша сигна:', attachment=img)


# принимаем сообщение !qrcode и значение, отправляем результат
@bot.on.message(text='!qrcode <name>')
async def qrcode(ans: Message, name):
    # вызываем функцию из другого файла
    qr.create_qrcode(name)
    # отправляем картинку на сервер и отправляем сообщение
    img = await photo_uploader.upload('img/qrcode.png')
    await ans.answer('ваш qr code:', attachment=img)


# принимаем сообщение !nft и отправляем результат
@bot.on.message(text='!nft')
async def nft(ans: Message):
    # производим случайный выбор картинки
    random_img = os.path.join(DIR, random.choice(os.listdir(DIR)))
    # обрезаем название, чтобы остались только цифры иначе будет img/nft/123.png
    nft_name0 = random_img.replace("img/", "")
    nft_name1 = nft_name0.replace("nft\\", "")
    nft_name = nft_name1.replace(".png", "")
    # отправляем картинку на сервер и отправляем сообщение
    img = await photo_uploader.upload(random_img)
    await ans.answer(f'ваш nft №{nft_name}:', attachment=img)


# принимаем сообщение !help и отправляем результат
@bot.on.message(text='!help')
async def help(ans: Message):
    await ans.answer('Привет, я БОТ!\n\nМой функционал:\n!help - список команд;\n\
        !pogoda - показываю погоду;\n!sign - генерирую сигну, пример !sign ВАШ ТЕКСТ;\n\
        !qrcode - генерирую qr код, пример !qrcode ВАШ ТЕКСТ;\n\
        !nft - генерирую одну случайную картинку из 3600;\n\n\
        Удачного использования!')


# принимаем любое сообщение и отправляем результат
@bot.on.message()
async def random_message(ans: Message):
    await ans.answer('Привет, напишите !help чтобы посмотреть все команды!')


# инициализируем бота
# перед запуском бота лучше удалить файлы
# img/sign.png
# img/weather.png
# img/qrcode.png
bot.run_forever()
