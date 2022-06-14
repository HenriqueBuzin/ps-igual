FROM python:3.10.5-slim-buster

WORKDIR /ps_equal_pyhon

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /ps_equal_python/src

CMD ["python3", "main.py"]
