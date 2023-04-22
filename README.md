# api_final
## Описание:


#### API для социальной сети, в которой пользователи могут публиковать записи/сообщения и просматривать сообщению других пользователей. Реализованы механизм комментариев к записям, возможность подписки на публикации интересующий авторов, регистрация пользователей. Для аутентификации используется JWT-токен.
## Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:marke1-web/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
source venv/scripts/activate

```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
# Примеры
### Примеры запросов к API:
#### POST-запрос на эндпоинт api/v1/posts/:


```
{
"text": "string",
"image": "string",
"group": 1
}
```
#### Ответ:

```
{
    "id": 1,
    "author": "username",
    "text": "string",
    "pub_date": "2023-07-17T15:17:24Z",
    "image": "string",
    "group": 1
}
```

#### GET-запрос на эндпоинт api/v1/posts/{post_id}/comments/:

```
[
    {
        "id": 1,
        "author": "username",
        "text": "string",
        "created": "2023-07-17T15:17:24Z",
        "post": 1
    },
    {
        "id": 2,
        "author": "username",
        "text": "string",
        "created": "2023-07-17T15:17:24Z",
        "post": 1
    }
]
```