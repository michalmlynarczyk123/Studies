import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import find_by_name, all_countries


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

    return render(request, 'basics/country.html', {
        'country': found_country
    })


def find_country_by_index(request, country_index):
    try:
        found_country = all_countries[country_index]
        redirect_path = reverse('country_by_name_url', args=[found_country["country"]])
        # return HttpResponse(f'{found_country["country"]} {found_country["capital"]}'
        # print(redirect_path)
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound(f'Kraj o indeksie {country_index} nie został znaleziony')


def country_list(request, country_count):
    found_countries = all_countries[:country_count]
    return render(request, 'basics/country_list.html', {
        'countries': found_countries,
        'country_count': country_count
    })


def first_html(request):
    response_data = """
        <h1>To jest HTML</h1>
        <ul>
            <li>Jeden</li>
            <li>Dwa</li>
            <li>Trzy</li>
        </ul>
    """

    response_data += '<h1>Dodane</h1>'
    for i in range(10):
        response_data += f'<p>{i}</p>'

    return HttpResponse(response_data)


def first_template(request):
    return render(request, 'basics/first_template.html')
