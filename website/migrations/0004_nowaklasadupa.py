# Generated by Django 3.0.5 on 2020-04-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_merge_20200419_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='NowaKlasaDupa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
            ],
        ),
    ]
