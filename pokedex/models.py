from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    type1 = models.CharField(max_length=200)
    type2 = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    hp = models.IntegerField()
    speed = models.IntegerField()
    front_default = models.CharField(max_length=200)
    back_default = models.CharField(max_length=200)
    front_shiny = models.CharField(max_length=200)
    back_shiny = models.CharField(max_length=200)

    def __str__(self):
        return self.name