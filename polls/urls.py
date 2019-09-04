from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/actor', views.search_movie, name='search_movie'),
    path('add/movie', views.add_movie, name='add_movie'),
    path('add/actor', views.add_actor, name='add_actor'),
    path('delete/actor', views.delete_actor, name='delete_actor'),
    path('delete/movie', views.delete_movie, name='delete_movie'),
    path('<int:movie_id>/', views.detail, name='detail'),
]