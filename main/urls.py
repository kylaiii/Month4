from django.urls import path
from . import views


urlpatterns = [
    path('films/<int:id>/', views.one_film),
    path('films/', views.films_list_view),
    path('directors/', views.directors),
    path('films_detail/<int:id>/', views.films_detail),
    path('director/<int:id>/', views.director_films),
    path('films/create/', views.create_film),
    path('director/create/', views.create_director),
    path('register/', views.registerr),
    path('login/', views.loginn),
    path('logout/', views.logout_view),
    path('search/', views.search),


]

