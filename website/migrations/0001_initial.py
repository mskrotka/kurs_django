# Generated by Django 3.0.5 on 2020-04-17 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadatkoweInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czas_trwania', models.PositiveSmallIntegerField(default=0)),
                ('gatunek', models.PositiveSmallIntegerField(choices=[(1, 'Sci-Fi'), (2, 'Horror'), (3, 'Dramat'), (4, 'Komedia'), (5, 'Inne')], default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=64, unique=True)),
                ('rok', models.PositiveSmallIntegerField(default=2000)),
                ('opis', models.TextField(default='')),
                ('premiera', models.DateField(blank=True, null=True)),
                ('imdb_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('plakat', models.ImageField(blank=True, null=True, upload_to='plakaty')),
                ('dodatkowe', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.DadatkoweInfo')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.PositiveSmallIntegerField(choices=[(1, 'Facebook'), (2, 'Instagram'), (3, 'LinkedIn')])),
                ('link', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recenzja', models.TextField(blank=True, default='')),
                ('gwiazdki', models.PositiveSmallIntegerField(default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Film')),
            ],
        ),
        migrations.CreateModel(
            name='Aktor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('filmy', models.ManyToManyField(to='website.Film')),
            ],
        ),
    ]
