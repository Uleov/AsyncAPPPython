# Практикум по асинхронности в Python: Уровень 1

Этот репозиторий содержит решения для 5 заданий первого уровня практикума по асинхронности в Python. Все решения выполнены в соответствии с требованиями: код простой и понятный для объяснения, без комментариев в файлах кода, а все текстовые сообщения переведены на русский язык.

## Структура проекта

### task_1: Консольный асинхронный таймер задач
* Файл кода: [async_timer.py](file:///c:/Users/artur/Desktop/AsyncPython/task_1/async_timer.py) (реализация корутин таймера с последовательным и конкурентным режимом запуска, а также выбором режима через аргумент `--mode`).
* Документация: [README.md](file:///c:/Users/artur/Desktop/AsyncPython/task_1/README.md) (описание работы и проверок).

### task_2: Консольный симулятор загрузок
* Файл кода: [download_simulator.py](file:///c:/Users/artur/Desktop/AsyncPython/task_2/download_simulator.py) (имитация конкурентной загрузки файлов, вывод красивой таблицы результатов, обработка ошибок и сравнение поведения `gather(return_exceptions=False)` и `gather(return_exceptions=True)` с корректным завершением (отменой) фоновых задач при ошибке).
* Документация: [README.md](file:///c:/Users/artur/Desktop/AsyncPython/task_2/README.md) (описание работы и проверок).

### task_3: Консольная очередь сообщений
* Файл кода: [message_queue.py](file:///c:/Users/artur/Desktop/AsyncPython/task_3/message_queue.py) (реализация шаблона Producer-Consumer с ограниченной очередью `maxsize=5`, тремя обработчиками, корректным жизненным циклом и выводом отчёта об обработанных сообщениях).
* Документация: [README.md](file:///c:/Users/artur/Desktop/AsyncPython/task_3/README.md) (описание работы и проверок).

### task_4: FastAPI-сервис задержек
* Файл кода: [delay_api.py](file:///c:/Users/artur/Desktop/AsyncPython/task_4/delay_api.py) (асинхронный API-сервис с `/ping` и двумя эндпоинтами для задержки: через path-параметр `/delay/{seconds}` и query-параметры `/delay?seconds=...&label=...`).
* Документация: [README.md](file:///c:/Users/artur/Desktop/AsyncPython/task_4/README.md) (описание работы и примеры curl-запросов).

### task_5: FastAPI мини-счётчик задач
* Файл кода: [task_counter_api.py](file:///c:/Users/artur/Desktop/AsyncPython/task_5/task_counter_api.py) (асинхронный API-сервис для работы с задачами: создание, чтение по ID, получение общего списка, перевод в статус `done` через PATCH-запрос, использующий in-memory словарь).
* Документация: [README.md](file:///c:/Users/artur/Desktop/AsyncPython/task_5/README.md) (описание работы и примеры curl-запросов).

## Требования к окружению

* Python 3.10 или новее.
* Сторонние библиотеки (для FastAPI-заданий 4 и 5):
  ```bash
  pip install fastapi uvicorn
  ```

## Запуск заданий

1. Задание 1:
   ```bash
   python task_1/async_timer.py --mode both
   ```
2. Задание 2:
   ```bash
   python task_2/download_simulator.py
   ```
3. Задание 3:
   ```bash
   python task_3/message_queue.py
   ```
4. Задание 4:
   ```bash
   uvicorn task_4.delay_api:app --reload
   ```
5. Задание 5:
   ```bash
   uvicorn task_5.task_counter_api:app --reload
   ```
