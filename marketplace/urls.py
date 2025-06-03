from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallerie/', views.gallerie, name='gallerie'),
    path('leistungen/', views.leistungen, name='leistungen'),
    path('fragen/', views.fragen, name='fragen'),
    path('furniture/<int:id>/', views.furniture_detail, name='furniture_detail'),

]