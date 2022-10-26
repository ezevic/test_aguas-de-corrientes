from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import index, PalabrasListView, palabra_detail_view, register, login_user

urlpatterns = [
    path('', index, name='index'),
    path('lista_palabra/', login_required(PalabrasListView.as_view()), name='lista'),
    path('palabra/<int:pk>', palabra_detail_view, name='palabra-detail'),
    path("register/", register, name="register"),
    path("login/", login_user, name="login_user"),
]

