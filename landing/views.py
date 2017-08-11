from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

# Create your views here.


def landing(request):
    name = "Anna"
    current_day = '14.07.2017'
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
    	print(request.POST)
    	print (form.cleaned_data)
    	data = form.cleaned_data
    	print(data["name"])

    	new_form = form.save()

    	# form = form.save() если будет эта строка, то
    	# форма после заполнения пропадёт

    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True) #product__is_active=True отключенные товары не попадают
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())