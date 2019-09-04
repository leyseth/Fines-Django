from django.urls import path
from . import views

app_name = 'infractions'

urlpatterns = [
	path('', views.index, name='index'),
	path('detail/<int:infractions_speed>', views.detail, name='detail'),
	path('read_json', views.read_json, name='read_json'),
]
