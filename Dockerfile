FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV DATABASE_URL=${DATABASE_URL}

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
