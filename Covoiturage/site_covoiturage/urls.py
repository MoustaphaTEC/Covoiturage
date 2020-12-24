from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conducteur/', views.conducteur, name='conducteur'),
    path('passager/', views.passage, name='passager'),
    path('trajetoire/', views.trajetoire, name='trajetoire'),
    path('trajet/<int:id>', views.show, name='show'),
    path('afficheConducteur/<int:id>', views.afficheConducteur, name='afficheConducteur'),
    path('affichePassager/<int:id>', views.affichePassager, name='affichePassager'),
    path('modifier/<int:id>', views.modifier, name='modifier'),
    path('supprimer/<int:id>', views.supprimer, name='supprimer'),
    path('creation/<int:id>', views.creation, name='creation'),
]
