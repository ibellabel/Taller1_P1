from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
    age = request.GET.get("age", "")               # kids / teens / adults
    searchTerm = request.GET.get("searchMovie", "")

    movies = Movie.objects.all()

    if age:
        movies = movies.filter(age_group=age)

    if searchTerm:
        movies = movies.filter(title__icontains=searchTerm)

    return render(request, "home.html", {
        "searchTerm": searchTerm,
        "movies": movies
    })

def about(request):
    return HttpResponse("<h1>Welcome to about page</h1>")
