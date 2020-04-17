from django.forms import ModelForm
from .models import Film, DadatkoweInfo, Ocena


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'opis', 'premiera', 'rok', 'imdb_rating', 'plakat']


class DodatkoweInfoForm(ModelForm):
    class Meta:
        model = DadatkoweInfo
        fields = ['czas_trwania', 'gatunek']


class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']


