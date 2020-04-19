from django.db import models
from .choices import social_links_list, gatunek_list


class DadatkoweInfo(models.Model):
    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(choices=gatunek_list(), default=5)

    def __str__(self):
        return f'{self.show_gatunek_name()}, {self.czas_trwania} min. '

    def show_gatunek_name(self):
        for i in gatunek_list():
            if self.gatunek == i[0]:
                return i[1]


class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default='')
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    plakat = models.ImageField(upload_to='plakaty', null=True, blank=True)
    dodatkowe = models.OneToOneField(DadatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tytul_z_rokierm()

    def tytul_z_rokierm(self):
        return f'{self.tytul} ({self.rok})'


class SocialLinks(models.Model):
    social_name = models.PositiveSmallIntegerField(choices=social_links_list())
    link = models.CharField(max_length=128)

    """ Wygenerowanie nazwy social media """
    def __str__(self):
        for i in social_links_list():
            if self.social_name == i[0]:
                return i[1]


class Ocena(models.Model):
    recenzja = models.TextField(default='', blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film)


class Rezyser(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film)

    def __str__(self):
        return self.imie
