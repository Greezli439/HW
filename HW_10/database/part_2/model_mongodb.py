from mongoengine import Document
from mongoengine.fields import StringField, BooleanField

class Consumer(Document):
    name = StringField()
    email = StringField()
    notified = BooleanField()