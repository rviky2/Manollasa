FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . /app/
RUN pip install gunicorn

CMD ["gunicorn", "new_manollasa.wsgi:application", "--bind", "127.0.0.1:8000"]
