<h1> 
     👾 Бот для ВК
</h1>

<h3>
Основная функция бота -  отправлять в личные сообщения информацию о погоде, случайные картинки, создавать qr коды на основе отправленного текста и делать сигны
</h3>



</br>



<h2>
  🛠️ Библиотеки для работы бота:
</h2>

- vkbottle==4.2.1
- pyowm==3.3.0
- Pillow==8.4.0
- qrcode==7.3.1
- translate==3.6.1



</br>



<h2>
  🚀 Зпуск приложения:
</h2>

- git clone https://github.com/ElishaFlacon/vk-bot-creating-group-post.git
- cd vk-bot-creating-group-post
- python -m venv <venv_name>
- source <venv_name>/Scripts/activate (linux) or <venv_name>/Scripts/activate (windows)
- pip install -r ./requirements.txt
- регистрируемся на сайте OWM и получаем ключ (https://openweathermap.org)
- добавте полученный ключ в код (weather_updater.pyw 7 строка)
- регистрируемся в ВК и создаем группу (https://vk.com/)
- получаем токен группы, предварительно в настройках группы включаем все разрешения для бота и longpull
- добавте токен группы (15 строка)
- измените путь до weather_update.pyw в weather function (25 строка)
- в коде измените город для которого хотите получать прогноз погоды (weather_updater.pyw 11 строка)
- по желанию можно включить функцию перевода описания погоды (weather_updater.pyw 25-26 строка) (у библиотеки ограниченное количество переводов)
- изменяем остальной код под свои нужды
- python main.py
<h3>
    Запускаем, не работет, ура! 🗿🚬
</h3>


</br>



<h2>
 📺 Демо:
</h2>
<p aligh="center">
<video src="https://user-images.githubusercontent.com/83610362/233343029-6000ecc6-cf45-464f-b813-b5fc264ab1a6.mp4" />
</p>



</br>



<h2>
⚡ Немного дополнительной информации:
</h2>

- На данный момент проект полностью реализован!
- P.S. Все баги и недочеты - это фичи
- Код проекта - говно, знаю, переписывать не буду это на память!




<br/>
<br/>
<br/>
<br/>
<br/>
<br/>



<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=d179b8&height=64&section=footer"/>
</p>

