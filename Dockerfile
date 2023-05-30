FROM python

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD  ["python3",  "assistant/Main_menu.py"]