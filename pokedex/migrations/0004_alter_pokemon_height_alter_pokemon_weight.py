# Generated by Django 4.1.3 on 2022-11-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_pokemon_delete_pokedex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(),
        ),
    ]
