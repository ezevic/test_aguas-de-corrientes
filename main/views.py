from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView


from .forms import PalindromoForm
from .models import Palindromo

# Create your views here.


def index(request):

    # function that checks if the 'palabra' input is 'palindromo'

    def if_palindromo(cadena):
        texto = str(cadena).lower().replace(" ", "").replace(",", "").replace(
            "á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        if texto == texto[::-1]:
            return True
        else:
            return False

    if request.method == 'POST':
        form = PalindromoForm(request.POST)
        if form.is_valid():
            palabra_form = form.cleaned_data.get('palabra')

            if Palindromo.objects.filter(palabra=palabra_form).exists():
                print('existe')
                palindromo = Palindromo.objects.get(palabra=palabra_form)
                print(palindromo)
                palindromo.save()
            else:
                print('no existe')
                palindromo = Palindromo(
                    palabra=palabra_form, check_palindromo=if_palindromo(palabra_form))
                palindromo.save()

            return redirect(f'palabra/{palindromo.pk}')

        else:
            print('formulario no valido')
            messages.error(
                request, 'Hubo un error al enviar el formulario. Verifica los campos e intentalo de nuevo.')
    else:
        form = PalindromoForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context=context)


# class based view to list all 'palabras' from the database

class PalabrasListView(ListView):


    model = Palindromo
    paginate_by = 20
    context_object_name = 'palabras'


# view function for a specify 'palabra'

def palabra_detail_view(request, pk):
    palabra = get_object_or_404(Palindromo, pk=pk)

    # function that determinate if a 'palabra' was created before.

    def same_date(date_created, date_updated):
        if date_created.replace(microsecond=0) == date_updated.replace(microsecond=0):
            return True
        else:
            return False

    context = {
        'palabra': palabra,
        'same_date': same_date(
            palabra.created_at, palabra.update_at)
    }

    return render(request, 'main/palindromo_detail.html', context=context)
