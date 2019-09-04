from django.shortcuts import render
from django.http import HttpResponse

import string
import json

def index(request):

    return render(request, 'index.html')

def detail(request, infraction_number):

    #infraction_number = 8
    #number = infraction_number
    json_data = open('C:/Users/leyseth/Documents/GitHub/Fines-Django/infractions.json').read()

    input_dict = json.loads(json_data)

    output_dict = [x for x in input_dict if x['infractions_speed'] == infraction_number]
    out = json.dumps(output_dict)
    #out = json_data["infraction_number"]
    return render(request, 'detail.html', {'out': out})
