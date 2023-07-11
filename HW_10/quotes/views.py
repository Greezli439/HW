from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quote, Author
from .forms import AuthorForm, QuoteForm
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

    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            authors_from_db = Author.objects.filter(name__in=request.POST.getlist('fullname'))
            for au in authors_from_db.iterator():
                new_note.authors.add(au)

            return redirect(to='quotes:quotes')
        else:
            return render(request, 'quotes/add_quote.html', {"authors": authors, 'quote_form': form})

    return render(request, 'quotes/add_quote.html', {"authors": authors, 'quote_form': QuoteForm()})


def author(request, id):
    author_data = Author.objects.get(pk=id)
    context = {'author_data': author_data}
    return render(request, 'quotes/author.html', context)
