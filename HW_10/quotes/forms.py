from django.forms import ModelForm, CharField, TextInput
from .models import Author, Quote

class AuthorForm(ModelForm):
    fullname = CharField(max_length=30, required=True, widget=TextInput())
    born_date = CharField(max_length=20, required=True, widget=TextInput())
    born_location = CharField(max_length=40, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(max_length=150, required=True, widget=TextInput())
    tags = CharField(max_length=150, required=True, widget=TextInput())
    author = CharField(max_length=30, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'tags']
        exclude = ['author']
