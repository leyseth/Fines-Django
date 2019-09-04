from django.shortcuts import render
from django.http import HttpResponse

import string

def index(request):

    return render(request, 'index.html')

def detail(request, infraction_number):

    json_data = open('C:/Users/leyseth/Documents/GitHub/Fines-Django/infractions.json').read()
    out = jsondata['infraction_number']
    return HttpResponse(out)
    #return render(request, 'quotes/detail.html', {'quote_list': quote_list})
