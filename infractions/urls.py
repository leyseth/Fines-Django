from django.urls import path
from . import views

app_name = 'infractions'

urlpatterns = [
	path('', views.index, name='index'),
	path('<str:infraction_number>/', views.detail, name='detail'),
	path('detail', views.detail, name='detail'),
]
