FROM python

WORKDIR /app

COPY . /app

EXPOSE 3000

RUN pip install -r requirements.txt

CMD  ["python3",  "main.py"]