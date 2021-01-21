from django.urls import path
from . import views

app_name = 'hangout'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
