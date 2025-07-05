# NSFW Image moderation FastAPI Service

Сервер на FastAPI, который принимает изображение и отправляет его на внешний API по адресу `https://nsfw-categorize.it/api/upload`.

---

## Запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/JohnLool/test-task/
cd test-task
```

2. Создайте виртуальное окружение и установите зависимости.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Или через Poetry
```bash
poetry install
poetry env activate
# далее скопировать результат в терминал
```
3. Запустите сервер:
```bash
uvicorn app.main:app --reload
```

---
## Пример запроса
```bash
curl -X POST -F "file=@example.jpg" http://localhost:8000/moderate
```

Если проверка пройдена:
```json
{
  "status": "OK"
}
```
Если изображение содержит NSFW-контент:
```json
{
  "status": "REJECTED",
  "reason": "NSFW content"
}
```