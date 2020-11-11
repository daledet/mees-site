from django.shortcuts import render


def start(request):
    return render(request, 'start.html', {})

    # import json
    # import requests

    # api_request = requests.get(
    #     "http://api.openweathermap.org/data/2.5/weather?id=3137115&appid=4fbcfd9147ff6df0e3ee3de039a4e70c&units=metric")

    # try:
    #     api = json.loads(api_request.content)

    # except Exception as e:
    #     api = "Error..."

    # return render(request, 'start.html', {'api': api})
