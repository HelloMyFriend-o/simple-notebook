# Записная книжка

1. Склонируйте репозиторий с помощью git
```bash
git clone https://github.com/HelloMyFriend-o/simple-notebook.git
```
2. Создайте и активируйте виртуальное окружение

3. Установите зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```
4. Переименуйте файл **.env(example)** в **.env**

5. Сгенерируйте Django SECRET_KEY (например тут: djecrety.ir) и присвойте соответствующей переменной в файле **.env**

6. Создайте БД PostgreSQL и заполните соответствующие переменные в файле **.env**

7. Перейдите в папку:
```bash
cd snotebook
```

8. Запустите приложение:
```bash
python manage.py runserver
```

9. Приложение будет доступно по адресу: http://127.0.0.1:8000/
