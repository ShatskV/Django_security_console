# Пульт охраны банка

Сайт пульта охраны банка, эмуляция посещения хранилища.

Содержит данные пропусков людей, их визитов в хранилище и проверку на подозрительные посещения.

Проект выполнен на Django.

## Как установить:

- Скачайте код

- Установите пакеты командой:

  ```
  pip install -r requirements.txt
  ```

- Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

- Создайте в корне проекта файл **.env** с переменными среды для подключения к базе данных, укажите секретный ключ и режим дебага, пример заполнения содержится в файле **.env.example**

## Запуск

- Запустите через проект через консоль:
  ```
  python3 manage.py runserver 0.0.0.0:8000
  ```


- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
