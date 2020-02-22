from django.shortcuts import render
import json
import requests

# Create your views here.
def home(request):
    #http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2020-02-22&distance=2&API_KEY=61A2D589-CED7-482B-B8D8-46473B0A4E54
    if request.method=='POST':
        zipcode=request.POST['zipcode']
        api_request=requests.get('http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode='+zipcode+'&date=2020-02-22&distance=2&API_KEY=61A2D589-CED7-482B-B8D8-46473B0A4E54')
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api='error'
        return render(request, 'home.html', {'api':api})
    else:
        api_request=requests.get('http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2020-02-22&distance=2&API_KEY=61A2D589-CED7-482B-B8D8-46473B0A4E54')
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api='error'
        return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})