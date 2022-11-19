# Generated by Django 4.1.3 on 2022-11-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('special_attack', models.IntegerField()),
                ('special_defense', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('front_default', models.CharField(max_length=200)),
                ('back_default', models.CharField(max_length=200)),
                ('front_shiny', models.CharField(max_length=200)),
                ('back_shiny', models.CharField(max_length=200)),
            ],
        ),
    ]
