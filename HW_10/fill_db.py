from mongoengine import connect
from mongoengine import Document
from mongoengine.fields import StringField, ListField, ReferenceField


connect(host='mongodb+srv://greezlistuding:UB1VnEMbXIJSxHph@cluster0.1iemlfa.mongodb.net/?retryWrites=true&w=majority')


class Authors(Document):
    fullname = StringField(unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors, reverse_delete_rule='CASCADE')
    quote = StringField()


data = Quotes.objects()
print(data)