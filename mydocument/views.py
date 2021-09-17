from django.shortcuts import render
import requests

def userdocument(request):
    userdta = requests.get('http://127.0.0.1:8080/api/user/')

    this = userdta.json()
    context = {
        'this': this,
    }
    return render(request, 'dashboard.html', context)