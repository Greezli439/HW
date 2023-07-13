from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import Author, Quote, Tag

class AuthorForm(ModelForm):
    fullname = CharField(max_length=30, required=True, widget=TextInput())
    born_date = CharField(max_length=20, required=True, widget=TextInput())
    born_location = CharField(max_length=40, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class TagForm(ModelForm):
    tag_name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag_name']


class QuoteForm(ModelForm):
    text = CharField(min_length=10, required=True, widget=Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Quote
        fields = ['text']
        exclude = ['tags', 'author']

    # quote = CharField(max_length=150, required=True, widget=TextInput())
    # author = CharField(max_length=150, required=True, widget=TextInput())
    # tags = CharField(max_length=50, required=True, widget=TextInput())
    #
    # class Meta:
    #     model = Quote
    #     fields = ['quote', 'author']
    #     exclude = ['tags']



