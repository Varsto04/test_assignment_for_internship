from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.template import loader
from .models import Weather
import json


def ping(request):
    return HttpResponse("<html><body>PONG</body></html>")


def health(request):
    return JsonResponse({"status": "HEALTHY"})


def list_weather(request):
    items = Weather.objects.all()
    tpl = loader.get_template('main/list.html')
    return HttpResponse(tpl.render({'items': items}, request))


def add_weather(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Only POST allowed')

    try:
        data = json.loads(request.body)
        city = data['city']
        temperature = int(data['temperature'])
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        return HttpResponseBadRequest(f'Invalid payload: {e}')

    obj = Weather.objects.create(city=city, temperature=temperature)

    return JsonResponse({'id': obj.id, 'city': obj.city, 'temperature': obj.temperature})
