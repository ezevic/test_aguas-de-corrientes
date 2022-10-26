from django.urls import path

from .views import index, PalabrasListView

urlpatterns = [
    path('', index, name='index'),
    path('lista_palabra', PalabrasListView.as_view(), name='lista')
]

