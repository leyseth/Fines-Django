from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
import redis
import string
# pattern : "movies":movieid:movieName:GenreName
        #   "actors":movieid:actor_name
r = redis.StrictRedis(host='localhost', port=6379, db=0,  charset="utf-8", decode_responses=True)
class Movie(object):
    def __init__(self, id=None, title=None, genre=None):
        self.id = id
        self.title = title
        self.genre = genre

class Actor(object):
        def __init__(self, name=None, movie_id=None):
                self.name = name
                self.movie_id = movie_id

movie_count = 1

def index(request):
        keys = r.keys('movies:*')
        movieslist = []
        for key in keys:
                m = key.split(":")
                movieslist.append(Movie(m[1],m[2],m[3]))
        movieslist.sort(key=lambda x: x.title)
        return render(request, 'polls/index.html', {'movie_name': movieslist})

def detail(request, movie_id):
        keys = r.keys("actors:" + str(movie_id) + ":*")
        movie_name = r.keys('movies:' + str(movie_id) + "*")[0].split(":")[2]
        actorlist = []
        for key in keys:
                a = key.split(":")
                actorlist.append(Actor(a[2],a[1]))
        actor_name = r.keys("actors:" + str(movie_id) + ":*")
        return render(request, 'polls/detail.html', {'actor_name': actorlist, 'movie_name': movie_name,'movie_id': movie_id})

def search_form(request):
    return render(request, 'polls/index.html', {})

def search_movie(request):
    if request.method == 'POST':
        word = request.POST['search_term']
        result_movies = r.keys("movies:*:" + word + ":*")
        movie = next(iter(result_movies), None)
        movie_id = movie.split(':')[1]
        return detail(request,movie_id)

def add_movie(request):
        if request.method == 'POST':
                movie_name = request.POST['movie_name']
                movie_genre = request.POST['movie_genre']
                global movie_count 
                movie_count += 1
                pattern = 'movies:' + str(movie_count) + ':' + movie_name + ':' + movie_genre
                r.set(pattern,"")
                return index(request)
        else:        
                return render(request, 'polls/add_movie.html', {})
        
def add_actor(request):
        if request.method == 'POST':
                movie_id = request.POST['movie_id']
                actor_name = request.POST['actor_name']
                pattern = "actors:" + movie_id + ":" + actor_name
                r.set(pattern,"")
                return index(request)

def delete_actor(request):
        if request.method == 'POST':
                movie_id = request.POST['movie_id']
                actor_name = request.POST['actor_name']
                pattern = "actors:" + movie_id + ":" + actor_name
                r.delete(pattern)
                return index(request)

def delete_movie(request):
        if request.method == 'POST':
                movie_id = request.POST['movie_id']
                movie_name = request.POST['movie_name']
                movie_genre = request.POST['movie_genre']
                pattern = "movies:" + movie_id + ":" + movie_name + ":" + movie_genre
                keys = r.keys('actors:' + movie_id + '*')
                for actor in keys:
                        r.delete(actor)
                r.delete(pattern)
                return index(request)