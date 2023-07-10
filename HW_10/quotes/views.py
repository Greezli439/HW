from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
from django.template import loader


def index(request):
    return HttpResponse('hi')

# def quotes(request):
#     tamplate = loader.get_template('quotes/index.html')
#     quotes_list = Quote.objects.order_by('-id')
#     context = {'quotes_list': quotes_list}
#     rendered_tamplate = tamplate.render(context, request)
#     return HttpResponse(rendered_tamplate)


def quotes(request):
    quotes_list = Quote.objects.order_by('-id')
    context = {'quotes_list': quotes_list}

    return render(request, 'quotes/index.html', context)
