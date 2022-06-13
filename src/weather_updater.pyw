from translate import Translator
from pyowm import OWM
from PIL import Image, ImageDraw, ImageFont


class Weather():
    # вставляем свой ключ сюда
    owm = OWM('ВАШ КЛЮЧ OWM')
    mgr = owm.weather_manager()

    # выбираем город-страну и записываем их в region
    region = mgr.weather_at_place('Tyumen, Russian')

    # смотрим показания погоды и записываем их в w
    w = region.weather

    # записываем показания температуры в цельсиях в all_temps
    all_temps = w.temperature('celsius')

    # записываем показания ветра в all_wind
    all_wind = w.wind()

    # записываем показания облочности в weater_detail
    weater_detail = str(w.detailed_status)
    # перевод weater_detail
    # tr = Translator(from_lang="en", to_lang="ru")
    # tr_weater_detail = tr.translate(weater_detail)

    # достаем из словоря с температурами основную температуру
    # также переводим их в строку и целое число чтобы было удобно использоваь
    # round округляет в большую сторону
    main_temp = str(int(round(all_temps['temp'])))
    feel_temp = str(int(round(all_temps['feels_like'])))

    # достаем скорость ветра в speed_wind
    # не переводим в целое число, просто зачем?
    speed_wind = str(float(all_wind['speed']))

    # достаем направление ветра в градусах deg_wind
    # не переводим в троку, чтобы было удобно исполльзовать в дальнейшем
    deg_wind = int(all_wind['deg'])

    # достаем влажность
    main_humidity = str(int(w.humidity))

    # достаем давление
    press = w.pressure['press']
    # используем формулу и переводим в МРТ
    press = str(int(round(press / 1.348)))

    # достаем видимость
    visibility = str(w.visibility_distance / 1000)

    # достаем облачность
    cloud = int(w.clouds)

    # переменная принимает направление ветра
    wind_direction = ""

    # deg_wind значение переводим в текстовую информацию
    if deg_wind > 5 and deg_wind < 40:
        wind_direction = "ССВ"
    elif deg_wind >= 40 and deg_wind <= 50:
        wind_direction = "СВ"
    elif deg_wind > 50 and deg_wind < 85:
        wind_direction = "СВВ"
    elif deg_wind >= 85 and deg_wind <= 95:
        wind_direction = "В"
    elif deg_wind > 95 and deg_wind < 130:
        wind_direction = "ЮВВ"
    elif deg_wind >= 130 and deg_wind <= 140:
        wind_direction = "ЮВ"
    elif deg_wind > 140 and deg_wind < 175:
        wind_direction = "ЮЮВ"
    elif deg_wind >= 175 and deg_wind <= 185:
        wind_direction = "Ю"
    elif deg_wind > 185 and deg_wind < 220:
        wind_direction = "ЮЮЗ"
    elif deg_wind >= 220 and deg_wind <= 230:
        wind_direction = "ЮЗ"
    elif deg_wind > 230 and deg_wind < 265:
        wind_direction = "ЮЗЗ"
    elif deg_wind >= 265 and deg_wind <= 275:
        wind_direction = "З"
    elif deg_wind > 275 and deg_wind < 310:
        wind_direction = "СЗЗ"
    elif deg_wind >= 310 and deg_wind <= 320:
        wind_direction = "СЗ"
    elif deg_wind > 320 and deg_wind < 355:
        wind_direction = "ССЗ"
    else:
        wind_direction = "С"


def create_weather_image():
    # ПИЛЛОВ
    # рисуем картинку
    img = Image.new('RGBA', (500, 500), '#99CCFF')
    idraw = ImageDraw.Draw(img)

    # приписываем шрифт
    headline = ImageFont.truetype('arial.ttf', size=32)
    minsize = ImageFont.truetype('arial.ttf', size=24)
    # отрисовываем текст
    # когда переводчик заработает убираем коменты с него и юзаем tr_weater_detail
    idraw.text((40, 20), f"Погода в Тюмени: {Weather.weater_detail}",
               font=minsize, fill=(0, 0, 0, 255))
    idraw.text((40, 100), f"Температура: {Weather.main_temp}°C",
               font=headline, fill=(0, 0, 0, 255))
    idraw.text((40, 140), f"По ощущениям: {Weather.feel_temp}°C",
               font=headline, fill=(0, 0, 0, 255))
    idraw.text((40, 200), f"Ветер: {Weather.speed_wind}м/с, {Weather.wind_direction}",
               font=headline, fill=(0, 0, 0, 255))
    idraw.text((40, 260), f"Давление: {Weather.press} мм рт. ст.",
               font=headline, fill=(0, 0, 0, 255))
    idraw.text((40, 320), f"Влажность: {Weather.main_humidity}%",
               font=headline, fill=(0, 0, 0, 255))
    idraw.text((40, 380), f"Облачность: {Weather.cloud}%",
               font=headline, fill=(0, 0, 0, 255))
    idraw.text((40, 440), f"Видимость: {Weather.visibility}км",
               font=headline, fill=(0, 0, 0, 255))

    # сохроняем - перезаписываем картинку
    img.save("img/weather.png", "PNG")


# стартуем
create_weather_image()
