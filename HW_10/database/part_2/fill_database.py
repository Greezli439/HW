from model_mongodb import Consumer
from db_connection import connect


def check_databse():
    data = Consumer.objects()
    for i in data:
        print(i.to_mongo().to_dict())


if __name__ == '__main__':
    check_databse()
