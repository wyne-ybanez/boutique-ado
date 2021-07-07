from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JANdGG0l9FclefAFwPebA5o4N2XFiHaNtFt7IScTwQEDFRfpwNdfCbuemiw6vsfO0wWRnEuKNeOfZTnpy0KoW4x00o3u8QKpj',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)