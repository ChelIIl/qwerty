from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Client
from .forms import user_register_form


def main_page(request):
    products = Product.objects.all()
    return render(request, 'market/main_page.html', {'Products': products, 'title': "Все товары"})

def product_info(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'market/product_info.html', {'Product': product})


def sign_in(request):
    return render(request, 'market/sign_in.html')


def register(request):
    if request.method == 'POST':
        form = user_register_form(request.POST)
        if form.is_valid():
            client_login = form.cleaned_data['login']
            db_client = Client.objects.filter(login=client_login)
            print(client_login, db_client)
            if db_client.exists():
                form.add_error(None, 'Пользователь с таким логином уже существует')
                return render(request, 'market/register.html', {'form': form})
            
            else:
                form.save()
                return redirect(sign_in)

    else:
        form = user_register_form()

    return render(request, 'market/register.html', {'form': form})
