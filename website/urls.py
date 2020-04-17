from django.urls import path
from website.views import front, nowy_film, edytuj_film, usun_film

urlpatterns = [
    path('', front, name='front'),
    path('nowy/', nowy_film, name='nowy_film'),
    path('edytuj/<int:id>', edytuj_film, name='edytuj_film'),
    path('usun/<int:id>', usun_film, name='skasuj_film'),

]
