from django.shortcuts import render
from django.http import HttpResponse
from .models import infraction

import string
import json

#def __init__(self):
#    infraction.objects.all().delete()
#
#    json_data = open('C:/Users/leyseth/Documents/GitHub/Fines-Django/infractions.json').read()
#
#    input_dict = json.loads(json_data)
#
#    for data in input_dict:
#        infraction.objects.create(street=data['street'], speed_limit=data['speed_limit'], infractions_speed=data['infractions_speed'])

def read_json(request):
    infraction.objects.all().delete()

    json_data = open('C:/Users/leyseth/Documents/GitHub/Fines-Django/infractions.json').read()

    input_dict = json.loads(json_data)

    for data in input_dict:
        infraction.objects.create(street=data['street'], speed_limit=data['speed_limit'], infractions_speed=data['infractions_speed'])

    return render(request, 'read_json.html')

def index(request):

    #infractions_list = infraction.objects.all()

    #return render(request, 'index.html', {'infractions_list': infractions_list})
    return render(request, 'index.html')

def detail(request, infractions_speed):

    #infraction_number = 8
    #number = infraction_number
    #output_dict = [x for x in input_dict if x['infractions_speed'] == infraction_number]

    #out = json_data["infraction_number"]

    i=infraction.objects.all().filter(infractions_speed__gte=infractions_speed).order_by('infractions_speed')


    return render(request, 'detail.html', {'infractions_list': i})
