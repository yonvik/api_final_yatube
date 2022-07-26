# Api_final_yatube

## О проекте
REST API для социальной сети yatube.
Позволяет производить действия с постами, комментариями, сообществами и подписками.

## Требования
- Python 3.7 
- Django 2.2.19
- Djangorestframework 3.16

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yonvik/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
### Примеры использования
**Получение списка постов**
GET запрос http://127.0.0.1:8000/api/v1/posts/
Ответ:
```
[
    {
        "id": 1,
        "author": "user",
        "text": "New post",
        "pub_date": "2022-03-10T20:40:55.107802Z",
        "image": null,
        "group": 1
    },
    {
        "id": 7,
        "author": "admin",
        "text": "string",
        "pub_date": "2022-07-26T16:44:49.436966Z",
        "image": null,
        "group": 2
    }
]
```
**Создание поста**
POST запрос http://127.0.0.1:8000/api/v1/posts/
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Ответ:
```
{
    "id": 7,
    "author": "admin",
    "text": "string",
    "pub_date": "2022-07-26T16:44:49.436966Z",
    "image": null,
    "group": 2
}
```
