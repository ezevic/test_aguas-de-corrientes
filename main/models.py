from queue import Empty
from django.db import models

# Create your models here.


class Palindromo(models.Model):
    palabra = models.CharField("Palabra", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    check_palindromo = models.BooleanField(
        "Es palindromo", null=False, blank=False)

    def __str__(self):
        return self.palabra
