from django.db import models
from mongoengine.fields import StringField, ListField, ReferenceField
from mongoengine import Document


class Authors(Document):
    fullname = StringField(unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors, reverse_delete_rule='CASCADE')
    quote = StringField()
