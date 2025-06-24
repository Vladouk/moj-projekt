# Вихідний образ
FROM python:3.10-slim

# Робоча директорія
WORKDIR /app

# Копіюємо залежності
COPY Lab1-py/requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту коду
COPY Lab1-py/ .

# Стандартна команда (можеш змінити)
CMD ["pytest"]

