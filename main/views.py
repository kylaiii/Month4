from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.http import HttpResponse

from main import models
from main.models import Film
from .models import *
from .forms import *

def logout_view(request):
    logout(request)
    return redirect('/')

def welcome(request):
    return render(request, 'welcome.html')
def search(request):
    search_word = request.GET.get('search_word')
    context = {
        'search_word': search_word,
        'films': Film.objects.filter(name__icontains=search_word)
    }
    print(context['films'])
    return render(request, 'search.html', context)


def registerr(request):
    context = {
        'form': UserCreateForm()
    }
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/films/')
        context['form'] = form
    return render(request, 'register.html', context)


def loginn(request):
    context = {
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/films/')
            else:
                return redirect('/login/')
    return render(request, 'login.html', context)



def create_film(request):

    context = {
        'form': FilmForm()
    }
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
        else:
            context['form'] = form
    return render(request, 'create_film.html', context)


def create_director(request):
    context = {
        'form': DirectorForm()
    }
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/directors/')
        else:
            context['form'] = form
    return render(request, 'create_director.html', context)

def about_us(request):
    return render(request, 'about_us.html')


def date_now(request):
    date = datetime.datetime.now()
    return render(request, 'date_now.html', {'date':date})

def films_detail(request, id):
    detail = get_object_or_404(models.Film, id=id)
    return render(request, 'films_detail.html', {'detail':detail})



def director_films(request, id):
    direct = get_object_or_404(models.Film, id = id)
    return render(request, 'director_id.html', {'director':direct})


PAGE_SIZE = 4

def films_list_view(request):
    page = int(request.GET.get('page', 1))
    all_films = Film.objects.all()
    films = all_films[(page - 1) * PAGE_SIZE: page * PAGE_SIZE]
    pages = (all_films.count() + PAGE_SIZE - 1) // PAGE_SIZE

    dict_ = {
        'films': films,
        'buttons': [i for i in range(1, pages + 1)],
        'prev_page': page - 1,
        'next_page': page + 1,
        'page': page,
        'pages': pages,
    }

    return render(request, 'all_films.html', context=dict_)

def directors(request):
    data = {
        'directors': Director.objects.all()
    }
    return render(request, 'director_id.html', data)



def one_film(request, id):
    try:
        film = Film.objects.get(id=id)
    except:
        return HttpResponse("Film not found")
    data = {
        'film': film
    }
    return render(request, 'one_film.html', data)




