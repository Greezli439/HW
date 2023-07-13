from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quote, Author, Tag

from .forms import AuthorForm, QuoteForm, TagForm
from django.template import loader
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse('hi')


def quotes(request):

    context = {'quotes_list': Quote.objects.all(),
               'tags_list': Tag.objects.all(),
               'authors_list': Author.objects.all()
               }

    return render(request, 'quotes/index.html', context)

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:quotes')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'author_form': AuthorForm()})

@login_required
def add_qoute(request):

    metadata = {
        'quote_form': QuoteForm(),
        'authors': Author.objects.all(),
        'tags': Tag.objects.all()
    }

    if request.method == 'POST':
        form_q = QuoteForm(request.POST)

        if form_q.is_valid():
            new_quote = form_q.save(commit=False)
            author_from_post = Author.objects.get(id=request.POST.get('authors'))
            new_quote.author_id = author_from_post
            new_quote.quote = request.POST.getlist('text')[0]
            new_quote.save()
            choice_tags = Tag.objects.filter(tag_name__in=request.POST.getlist('tags'))
            print(choice_tags, request.POST.getlist('tags'))
            for tag in choice_tags:
                print(tag.id)
                new_quote.tags.add(tag)


            return redirect(to='quotes:quotes')
        else:
            return render(request, 'quotes/add_quote.html', metadata)

    return render(request, 'quotes/add_quote.html', metadata)


def add_tag(request):
    metadata = {
    'tag_form': TagForm()
    }

    if request.method == 'POST':
        form_t = TagForm(request.POST)

        if form_t.is_valid():
            new_tag = form_t.save()
            new_tag.save()
            return redirect(to='quotes:quotes')
        else:
            return render(request, 'quotes/add_tag.html', metadata)

    return render(request, 'quotes/add_tag.html', metadata)


def author(request, id):
    author_data = Author.objects.get(pk=id)
    context = {'author_data': author_data}
    return render(request, 'quotes/author.html', context)


if __name__ == '__main__':
    pass