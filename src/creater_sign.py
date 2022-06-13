from PIL import Image, ImageDraw, ImageFont


def create_sign(name):
    # открываем фото из папки
    photo1 = Image.open("img/rectangle.png")
    # создаем переменную, для удобства
    idraw = ImageDraw.Draw(photo1)
    # прописываем шрифт
    font = ImageFont.truetype("arial.ttf", size=52)
    # рисуем
    idraw.text((400, 200), name, font=font)
    # сохроняем
    photo1.save('img/sign.png')
