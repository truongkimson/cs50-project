from django.urls import path
from . import views

app_name = 'hangout'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('discover/', views.discover, name='discover'),
    path('<int:hangout_id>/detail/', views.detail, name='detail'),
    path('<int:hangout_id>/modify/', views.modify, name='modify'),
    path('<int:hangout_id>/delete/', views.delete, name='delete'),
]
