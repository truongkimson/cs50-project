from django.urls import path
from . import views

app_name = 'hangout'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('discover/', views.discover, name='discover'),
]
