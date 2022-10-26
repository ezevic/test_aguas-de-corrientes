from django.db import models
from django.urls import reverse


# Create your models here.


class Palindromo(models.Model):
    palabra = models.CharField("Palabra", max_length=100)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    update_at = models.DateTimeField(auto_now=True)
    check_palindromo = models.BooleanField(
        "Es palindromo", null=False, blank=False)

    def __str__(self):
        return self.palabra

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this 'palabra'."""
        return reverse('palabra-detail', args=[str(self.id)])

    
    class Meta:
        ordering = ['update_at']