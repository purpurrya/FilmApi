# FilmApi

Пет-проект, выполненный на основе руководства Патиля Ганешкумара "Django Rest API's Demystified" и представляющий собой API для учёта фильмов и сериалов: стриминговые платформы, список к просмотру и отзывы. Одни и те же сущности намеренно реализованы через разные подходы DRF.

## Технологии

- Python
- Django
- Django REST Framework
- SQLite
- ruff
- pre-commit
- uv
- Docker

## Развёртывание

### Клонирование репозитория

```bash
git clone https://github.com/purpurrya/FilmApi.git
cd FilmApi
```

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

Все пути указаны относительно префикса `/api/serializers_views/`.

### Watchlist — базовый `Serializer`

- `GET /watchlist-basic-serializer/` — список
- `POST /watchlist-basic-serializer/` — создание
- `PUT /watchlist-basic-serializer/<pk>/` — полное обновление
- `PATCH /watchlist-basic-serializer/<pk>/` — частичное обновление
- `DELETE /watchlist-basic-serializer/<pk>/` — удаление

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

- `GET /wathclist-hm-serializer/` — список
- `POST /wathclist-hm-serializer/` — создание
- `GET /wathclist-detail-hm-serializer/<pk>/` — детальная информация
- `PUT /wathclist-detail-hm-serializer/<pk>/` — полное обновление
- `PATCH /wathclist-detail-hm-serializer/<pk>/` — частичное обновление
- `DELETE /wathclist-detail-hm-serializer/<pk>/` — удаление

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
