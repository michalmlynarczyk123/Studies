import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import find_by_name


# Create your views here.

def hello_world(request):
    return HttpResponse('Witaj świecie z Django!')


def current_date(request):
    return HttpResponse(f'Czas odpowiedzi: {str(datetime.datetime.now())}')


counter = 0


def view_hits(request):
    global counter
    counter += 1
    return HttpResponse(f'Ten widok został wywołany {counter} razy')


def find_country_by_name(request, country_name):
    found_country = find_by_name(country_name)
    if found_country is None:
        return HttpResponseNotFound(f'Kraj {country_name} nie został znaleziony')

    return HttpResponse(f'{found_country["country"]} {found_country["capital"]}')
