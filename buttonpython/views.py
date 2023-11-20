import requests
import json
from django.shortcuts import render


def temperature(request):

    response = requests.get('https://7arx9lyrj8.execute-api.us-west-2.amazonaws.com/prod/dht')

    print(response.status_code)


    json_clean = json.dumps(response.json(), indent=4)
    json_clean = json.loads(json_clean)
    temp = json_clean['Temperature']
    light = json_clean['Light Intensity']
    ph_value = json_clean['Ph Value']
    water_level = json_clean['Water Level']
    humidity = json_clean['Humidity']
  

    context = {
        'temp' : temp,
        'light': light,
        'ph': ph_value,
        'water': water_level,
        'humidity': humidity

    }

    return render(request, 'home.html', context = context )


















