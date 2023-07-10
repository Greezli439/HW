from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=30)
    born_date = models.CharField(max_length=20)
    born_location = models.CharField()
    description = models.TextField()


class Quote(models.Model):
    quote = models.TextField()
    tags = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
