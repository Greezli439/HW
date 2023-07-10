from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE


class Author(Model):
    fullname = CharField(max_length=30)
    born_date = CharField(max_length=25)
    born_location = CharField()
    description = TextField()

    def __str__(self):
        return self.fullname


class Quote(Model):
    quote = TextField()
    tags = TextField()
    author = ForeignKey(Author, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.quote
