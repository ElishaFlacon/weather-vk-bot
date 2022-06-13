import qrcode


def create_qrcode(data):
    # генерируем qr-код
    img = qrcode.make(data)
    # сохраняем img в файл
    img.save("img/qrcode.png")
