from django.http import HttpResponse, Http404
from pprint import pprint
import json
from django.core import serializers

from .models import Continent, Country


def continent_json(request, continent_code):
    try:
        continent_data = Continent.objects.get(code=continent_code)
        countries_of_continent = continent_data.countries.all()

        output = {}
        for c in countries_of_continent:
            output[c.code] = c.name;

        json_dump = json.dumps(output)

        callback = request.GET.get('callback')
        if callback is not None:
            json_dump = callback + "("+json_dump+")"

        return HttpResponse(json_dump, content_type="application/json")

    except Continent.DoesNotExist:
        raise Http404("Continent does not exist")


def country_json(request, continent_code, country_code):
    try:
        continent = Continent.objects.get(code=continent_code);
        try:
            country = Country.objects.get(code=country_code, continent_id=continent.id)

            output = {
                "area": country.area,
                "population": country.population,
                "capital": country.capital
            }

            json_dump = json.dumps(output)

            callback = request.GET.get('callback')
            if callback is not None:
                json_dump = callback + "("+json_dump+")"

            return HttpResponse(json_dump, content_type="application/json")
        except Country.DoesNotExist:
            raise Http404("Country does not exist")
    except Continent.DoesNotExist:
        raise Http404("Continent does not exist")
