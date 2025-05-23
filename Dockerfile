FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate --noinput

RUN python manage.py collectstatic --no-input

ENV PORT 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
