# Сайт для барбершопа HotMode

## Описание

Cайт позволяет записывать клиентов, изменять прайс-лист, акции, информацию о мастерах и их работах.

Благодаря данному проету барбершоп сможет эффективнее привлекать новых клиентов, развивать свой бизнес и улучшать качество обслуживания, что приведет к повышению удовлетворенности клиентов.

В дальнейшем я планирую интегрировать его с социальными сетями, поработать над улучшением SEO-оптимизации сайта, чтобы повысить его позицию в результатах поиска.

## Установка на компютер

Клонировать репозиторий и перейти в него в командной строке:
`git clone git@github.com:P1oot/HotMode.git`
`cd HotMode`

Cоздать и активировать виртуальное окружение:
`python -m venv venv`
`source venv/bin/activate`

Установить зависимости из файла requirements.txt:
`python -m pip install --upgrade pip`
`cd hot_mode`
`pip install -r requirements.txt`

Изменить БД:
Перейти в `HotMode/hot_mode/settings.py`, либо `nano hot_mode/settings.py`
Изменить параметр `IS_POSTGRES` на `False`

Выполнить миграции:
`python manage.py migrate`

Запустить проект:
`python manage.py runserver`

## Установка на сервер.

Клонировать репозиторий и перейти в него в командной строке:
`git clone git@github.com:P1oot/infra_sp2.git`
`cd HotMode`

Создать и заполнить файл .env:
`cd infra`
`touch .env`
`nano .env`
*Пример заполнения .env ниже

Запустите docker-compose:
`docker-compose up -d`

Выполнить миграции:
`docker-compose exec web python manage.py migrate`

Создать суперпользователя:
`docker-compose exec web python manage.py createsuperuser`

Подключить статику:
`docker-compose exec web python manage.py collectstatic --no-input`

Остановить контейнеры можно комадой:
`docker-compose stop`

## *Пример заполнения .env
`DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql`

`DB_NAME=postgres # имя базы данных`

`POSTGRES_USER=postgres # логин для подключения к базе данных`

`POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)`

`DB_HOST=db # название сервиса (контейнера)`

`DB_PORT=5432 # порт для подключения к БД`