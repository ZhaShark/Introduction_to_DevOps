FROM python:3.11

WORKDIR /app

COPY requirements .

RUN pip install --no-cache-dir -r requirements

COPY . .

EXPOSE 5000

ENV FLASK_APP=hello.py

CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]

