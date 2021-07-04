from django.urls import path
from . import views

urlpatterns = [
    path('pseudo_search', views.autocomplete, name='autocomplete'),
    path('search', views.search, name= 'search'),
]