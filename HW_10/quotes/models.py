from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, ManyToManyField


class Author(Model):
    fullname = CharField(max_length=30)
    born_date = CharField(max_length=25)
    born_location = CharField()
    description = TextField()

    def __str__(self):
        return self.fullname


class Tag(Model):
    tag_name = CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.tag_name


class Quote(Model):
    quote = TextField()
    tags = ManyToManyField(Tag)
    author = ForeignKey(Author, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.quote


if __name__ == '__main__':
    quotes_list = Quote.objects.all()
    print(quotes_list)