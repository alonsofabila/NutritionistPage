from django.db import models
from django.conf import settings


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    sex_choices = [("Male", "Male"),
                   ("Female", "Female"), ]
    sex = models.CharField(max_length=10, blank=False, null=False, choices=sex_choices)
    height = models.CharField(max_length=6, blank=False, null=False)
    weight = models.CharField(max_length=6, blank=False, null=False)
    exersice_choices = [("Yes", "yes"),
                        ("No", "no"), ]
    exersice = models.CharField(max_length=10, blank=False, null=False, choices=exersice_choices)
    nutritionist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return 'Client: ' + self.first_name + ' ' + self.last_name + ' Sex: ' + self.sex + ' Exercise: ' + self.exersice
