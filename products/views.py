from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key #уникальный идентификатор
    if not session_key:
    	request.session.cycle_key() #если пользователь не авторизован

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())