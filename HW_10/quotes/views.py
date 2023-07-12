from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quote, Author, Tag
from .forms import AuthorForm, QuoteForm, TagForm
from django.template import loader
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse('hi')

# def quotes(request):
#     tamplate = loader.get_template('quotes/index.html')
#     quotes_list = Quote.objects.order_by('-id')
#     context = {'quotes_list': quotes_list}
#     rendered_tamplate = tamplate.render(context, request)
#     return HttpResponse(rendered_tamplate)


def quotes(request):
    quotes_list = Quote.objects.all()
    context = {'quotes_list': quotes_list}

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
        'tag_form': TagForm(),
        'author_form': AuthorForm(),
        'authors': Author.objects.all(),
        'tags': Tag.objects.all()
    }

    if request.method == 'POST':
        form_q = QuoteForm(request.POST)
        form_t = TagForm(request.POST)
        form_a = AuthorForm(request.POST)
        if form_q.is_valid() and form_t.is_valid() and form_a.is_valid():
            new_quote = form_q.save(commit=False)
            author_from_post = form_a.save()
            new_quote.author = author_from_post
            new_quote.save()
            tags = form_t.save()
            tags_db_object = Tag.objects.filter(name__in=request.POST.getlist('tag_name'))
            for tag in tags_db_object.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotes:quotes')
        else:
            return render(request, 'quotes/1.html', metadata)


    return render(request, 'quotes/add_quote.html', metadata)


def author(request, id):
    author_data = Author.objects.get(pk=id)
    context = {'author_data': author_data}
    return render(request, 'quotes/author.html', context)
