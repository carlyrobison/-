FROM python:3.9.16

RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "api_libs/main.py"]
