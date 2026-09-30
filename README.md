# FilmPlatform

Пет-проект, выполненный на основе руководства Патиля Ганешкумара "Django Rest API's Demystified", представляет собой API для учёта фильмов и сериалов: платформы стриминга, список к просмотру  и отзывы. 
Одни и те же сущности намеренно реализованы через разные подходы DRF для практики.

## Технологии

- Python
- Django
- Django REST Framework
- SQLite
- python-decouple
- ruff
- pre-commit
- uv
- Docker

## Развёртывание

### Клонирование репозитория

```bash
git clone https://github.com/purpurrya/FilmPlatform.git
cd FilmPlatform
```

### Настройка окружения

```bash
cp .env.example .env
```

В `.env` нужно задать `DJANGO_SECRET_KEY` (любую случайную строку).

### Docker

```bash
docker compose up --build
```

### Локально

Установка зависимостей:

```bash
uv sync
```

Применение миграций:

```bash
uv run manage.py migrate
```

Запуск сервера:

```bash
uv run manage.py runserver
```

API будет доступно по адресу:

```
http://localhost:8000/api/serializers_views/
```

Админка Django — по адресу `http://localhost:8000/admin/` (предварительно создать суперпользователя: `uv run manage.py createsuperuser`).

## Линтинг

```bash
uv run ruff check
uv run ruff format
```

Перед коммитом дополнительно прогоняются хуки `pre-commit` (настроены в `.pre-commit-config.yaml`).

## API

Все пути указаны относительно префикса `/api/serializers_views/`. Роуты и классы вьюх сгруппированы по сущности (Watchlist, Stream Platform, Review), а внутри Watchlist — по используемому подходу DRF, от простого к сложному.

### Watchlist — базовый `Serializer`

- `GET /watchlist-basic-serializer/` — список
- `POST /watchlist-basic-serializer/` — создание
- `PUT /watchlist-basic-serializer/<pk>/` — полное обновление
- `PATCH /watchlist-basic-serializer/<pk>/` — частичное обновление
- `DELETE /watchlist-basic-serializer/<pk>/` — удаление

### Watchlist — `BaseSerializer`

- `GET /watchlist-base-serializer/` — список (кастомная сериализация через `to_representation`/`to_internal_value`)

### Watchlist — `ModelSerializer`

- `GET /watchlist-model-serializer/` — список
- `POST /watchlist-model-serializer/` — создание
- `PUT /watchlist-model-serializer/<pk>/` — полное обновление
- `PATCH /watchlist-model-serializer/<pk>/` — частичное обновление
- `DELETE /watchlist-model-serializer/<pk>/` — удаление

### Watchlist — кастомный `ListSerializer`

- `GET /watchlist-list-serializer/` — список
- `POST /watchlist-list-serializer/` — создание одного или нескольких объектов за раз (массовое создание через `bulk_create`)

### Watchlist — `HyperlinkedModelSerializer`

- `GET /watchlist-hm-serializer/` — список
- `POST /watchlist-hm-serializer/` — создание
- `GET /watchlist-detail-hm-serializer/<pk>/` — детальная информация
- `PUT /watchlist-detail-hm-serializer/<pk>/` — полное обновление
- `PATCH /watchlist-detail-hm-serializer/<pk>/` — частичное обновление
- `DELETE /watchlist-detail-hm-serializer/<pk>/` — удаление

### Watchlist — `GenericAPIView`

- `GET /watchlist-generic-api/` — список (с поиском, сортировкой и пагинацией)
- `POST /watchlist-generic-api/` — создание
- `GET /watchlist-detail-generic-api/<title>/` — объект по названию (`title` как lookup-поле)

### Watchlist — `GenericAPIView` + `mixins`

- `GET /watchlist-list-model-mixin/` — список
- `POST /watchlist-create-model-mixin/` — создание
- `GET /watchlist-retrieve-model-mixin/<pk>/` — объект по id
- `PUT /watchlist-update-model-mixin/<pk>/` — полное обновление
- `PATCH /watchlist-update-model-mixin/<pk>/` — частичное обновление
- `DELETE /watchlist-destroy-model-mixin/<pk>/` — удаление

### Watchlist — готовые generic-вьюхи (`generics`)

- `GET /watchlist-list-api/` — список
- `POST /watchlist-create-api/` — создание
- `GET /watchlist-list-create-api/` — список
- `POST /watchlist-list-create-api/` — создание
- `GET /watchlist-retrieve-api/<title>/` — объект по названию (`title` как lookup-поле)
- `PUT /watchlist-update-api/<pk>/` — полное обновление
- `PATCH /watchlist-update-api/<pk>/` — частичное обновление
- `DELETE /watchlist-destroy-api/<pk>/` — удаление
- `GET /watchlist-retrieve-update-api/<pk>/` — объект по id
- `PUT /watchlist-retrieve-update-api/<pk>/` — полное обновление
- `PATCH /watchlist-retrieve-update-api/<pk>/` — частичное обновление
- `GET /watchlist-retrieve-destroy-api/<pk>/` — объект по id
- `DELETE /watchlist-retrieve-destroy-api/<pk>/` — удаление
- `GET /watchlist-retrieve-update-destroy-api/<pk>/` — объект по id
- `PUT /watchlist-retrieve-update-destroy-api/<pk>/` — полное обновление
- `PATCH /watchlist-retrieve-update-destroy-api/<pk>/` — частичное обновление
- `DELETE /watchlist-retrieve-update-destroy-api/<pk>/` — удаление

### Stream Platform

- `GET /streamplatform-basic-serializer/<pk>/` — платформа по id (обычный `Serializer`)
- `GET /streamplatform-detail-hm-serializer/<pk>/` — платформа по id (`HyperlinkedModelSerializer`)

### Отзывы

- `GET /reviewlist-basic-serializer/` — список отзывов

## Структура проекта

- `manage.py` — точка входа управления Django
- `drfproject/` — настройки проекта (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`)
- `project_setup/` — приложение с моделью `StreamPlatform`
- `watchlist_app/` — приложение с моделями `WatchList` и `Review`
- `serializers_views/api/` — сериализаторы (`serializers.py`), вьюхи (`views.py`), роуты (`urls.py`) и кастомные поля (`fields.py`)
- `db.sqlite3` — база данных SQLite
- `Dockerfile`, `docker-compose.yml` — контейнеризация
- `pyproject.toml`, `uv.lock` — зависимости и их версии
- `.pre-commit-config.yaml` — конфигурация pre-commit хуков
