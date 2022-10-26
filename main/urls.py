from django.urls import path

from .views import index, PalabrasListView, palabra_detail_view

urlpatterns = [
    path('', index, name='index'),
    path('lista_palabra', PalabrasListView.as_view(), name='lista'),
    path('palabra/<int:pk>', palabra_detail_view, name='palabra-detail'),
]

