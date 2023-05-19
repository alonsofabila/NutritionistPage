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
    nutritionist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Consult(models.Model):
    consult_date = models.DateField(auto_now_add=True, blank=False, null=False)
    new_weight = models.CharField(max_length=6, blank=False, null=False)
    observation = models.TextField(blank=True, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nutritionist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Consult: {self.consult_date}' + ' ' + self.new_weight + ' ' + self.observation
