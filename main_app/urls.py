from django.urls import path
from . import views

urlpatterns = [
    # define a root path using an empty string and map it to the view.home view function
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.bird_index, name='bird-index'),
]