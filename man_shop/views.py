from django.shortcuts import render,get_object_or_404
from man_shop import models

#Неполная информация
def product_view(request):
    product = models.Man_shop.objects.all()
    return render(request, 'product/product.html', {'product': product})

#Полная инофрмация

def product_deatil(request,id):
    product_id = get_object_or_404(models.Man_shop, id=id)
    return render(request, 'product/product_detail.html', {'product_id': product_id})


