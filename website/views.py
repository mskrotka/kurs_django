from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Film, SocialLinks, DadatkoweInfo, Ocena
from .forms import FilmForm, DodatkoweInfoForm, OcenaForm

wszystkie = Film.objects.all()
social_links = SocialLinks.objects.all()

context = {
    'filmy': wszystkie,
    'social': social_links
}


def front(request):
    return render(request, 'front.html', context)


@login_required()
def nowy_film(request):
    czy_nowy = True
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)

    if form_film.is_valid() and form_dodatkowe.is_valid():
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(front)

    return render(request, 'film_form.html', {'form': form_film,
                                              'form_dodatkowe': form_dodatkowe,
                                              'czy_nowy': czy_nowy})


@login_required()
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)

    oceny = Ocena.objects.filter(film=film)

    try:
        dodatkowe = DadatkoweInfo.objects.get(film=film.id)
    except DadatkoweInfo.DoesNotExist:
        dodatkowe = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)
    ocena_form = OcenaForm(request.POST or None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            ocena = ocena_form.save(commit=False)
            ocena.film = film
            ocena.save()

    if form_film.is_valid() and form_dodatkowe.is_valid():
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(front)

    return render(request, 'film_form.html', {'form': form_film,
                                              'form_ocena': ocena_form,
                                              'oceny': oceny,
                                              'form_dodatkowe': form_dodatkowe})


@login_required()
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(front)

    return render(request, 'potwierdz.html', {'film': film})
