from django.shortcuts import render
from django.http import HttpResponse
from .models import Name
import requests
# Create your views here.
def home(request):
    print(request.POST)
    if request.method=='POST':
        name=request.POST.get('name')
        print(request.POST.get('email'))
        Name.objects.create(name=name)
        url="http://localhost:9000/"
        data = {
           'email': request.POST.get('email')
        }
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        #requests.post(url, data={key: value}, json={key: value}, args)
        response = requests.post(url,data=data, json=data)
    names=Name.objects.all()
    return render(request,"one.html",{'names':names})


'''

import requests

# Define the URL where the request will be sent
url = 'https://example.com/api'

# Define the data to be sent in the POST request
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# Optionally, you can include headers
headers = {
    'Content-Type': 'application/json'
}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Check the response
if response.status_code == 200:
    print('Request was successful')
    print('Response:', response.json())
else:
    print('Request failed')
    print('Status code:', response.status_code)
    print('Response:', response.text)
'''