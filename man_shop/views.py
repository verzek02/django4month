from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from man_shop import models,forms

#Неполная информация
def product_view(request):
    product = models.Man_shop.objects.all()
    return render(request, 'product/product.html', {'product': product})

#Полная инофрмация

def product_detail(request,id):
    product_id = get_object_or_404(models.Man_shop, id=id)
    return render(request, 'product/product_detail.html', {'product_id': product_id})


#Добавление товара
def create_product_view(request):
    method = request.method
    if method == "POST":
        form = forms.Man_shop_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Товар успешно добавлен!')
    else:
        form = forms.Man_shop_form()
    return render(request, "crud/create_product.html", {'form': form})



#Удаление товара

def delete_product(request, id):
    product_id = get_object_or_404(models.Man_shop, id=id)
    product_id.delete()
    return HttpResponse('Товар удален')


#Обновление товара

def update_product(request,id):
    product_id = get_object_or_404(models.Man_shop, id=id)
    if request.method == 'POST':
        form = forms.Man_shop_form(instance=product_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Товар успешно изменён')
    else:
        form = forms.Man_shop_form(instance=product_id)
    context = {
        'form': form,
        'product_id': product_id
    }
    return render(request, 'CRUD/update_product.html', context)




