# Задание 5:

## Что реализовано
* FastAPI приложение с хранением задач в памяти процесса.
* Эндпоинт `POST /tasks` для создания задачи с начальным статусом created (отклонение пустых заголовков).
* Эндпоинт `GET /tasks/{task_id}` для поиска и возврата задачи по её идентификатору.
* Эндпоинт `GET /tasks` для получения списка всех задач в памяти.
* Эндпоинт `PATCH /tasks/{task_id}/done` для завершения задачи (перевод статуса в done).

## Как запустить
Запустите сервер из папки задания:
```bash
uvicorn task_counter_api:app --reload
```

## Примеры запросов (HTTP-клиент)

### 1. Создание задачи (POST /tasks)
Запрос:
```bash
curl -X POST http://127.0.0.1:8000/tasks \
     -H "Content-Type: application/json" \
     -d "{\"title\": \"Изучить asyncio\"}"
```
Ответ (HTTP 201):
```json
{
  "id": "e6a0d4c8-356c-48c0-82ab-264627d3ab14",
  "title": "Изучить asyncio",
  "status": "created"
}
```

### 2. Получение списка задач (GET /tasks)
Запрос:
```bash
curl -X GET http://127.0.0.1:8000/tasks
```
Ответ:
```json
[
  {
    "id": "e6a0d4c8-356c-48c0-82ab-264627d3ab14",
    "title": "Изучить asyncio",
    "status": "created"
  }
]
```

### 3. Перевод задачи в статус "done" (PATCH /tasks/{id}/done)
Запрос:
```bash
curl -X PATCH http://127.0.0.1:8000/tasks/e6a0d4c8-356c-48c0-82ab-264627d3ab14/done
```
Ответ:
```json
{
  "id": "e6a0d4c8-356c-48c0-82ab-264627d3ab14",
  "title": "Изучить asyncio",
  "status": "done"
}
```

### 4. Ошибка при неизвестном ID
Запрос:
```bash
curl -i -X GET http://127.0.0.1:8000/tasks/non-existent-id
```
Ответ (HTTP 404):
```
HTTP/1.1 404 Not Found
...
{"detail":"Задача не найдена"}
```

### 5. Ошибка при пустом заголовке
Запрос:
```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
     -H "Content-Type: application/json" \
     -d "{\"title\": \"   \"}"
```
Ответ (HTTP 400):
```
HTTP/1.1 400 Bad Request
...
{"detail":"Название задачи не может быть пустым"}
```
