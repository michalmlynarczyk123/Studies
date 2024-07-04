from django.db import models
import json


# Create your models here.

def load_countries():
    with open('basics/country_info.json', encoding='UTF-8') as file:
        return json.load(file)


def find_by_name(name: str):
    for country in all_countries:
        if country['country'].casefold() == name.casefold():
            return country
    return None


all_countries = load_countries()
