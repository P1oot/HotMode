FROM python:3.9.13-slim

WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
# CMD ["python", "manage.py", "runserver", "0:8000"]
CMD ["gunicorn", "hot_mode.wsgi:application", "--bind", "0:8000" ]
