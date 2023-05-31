from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from man_shop import models,forms
from django.views import generic


#Неполная информация
class PersonView(generic.ListView):
    template_name = 'product/product.html'
    queryset = models.Man_shop.objects.all()

    def get_queryset(self):
        return models.Man_shop.objects.all()

# def product_view(request):
#     product = models.Man_shop.objects.all()
#     return render(request, 'product/product.html', {'product': product})

#Полная инофрмация
class PersonDetailView(generic.DetailView):
    template_name = 'product/product_detail.html'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Man_shop, id=person_id)

# def product_detail(request,id):
#     product_id = get_object_or_404(models.Man_shop, id=id)
#     return render(request, 'product/product_detail.html', {'product_id': product_id})


#Добавление товара
class CreateProductView(generic.CreateView):
    template_name = "crud/create_product.html"
    form_class = forms.Man_shop_form
    queryset = models.Man_shop.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateProductView, self).form_valid(form=form)
# def create_product_view(request):
#     method = request.method
#     if method == "POST":
#         form = forms.Man_shop_form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Товар успешно добавлен!')
#     else:
#         form = forms.Man_shop_form()
#     return render(request, "crud/create_product.html", {'form': form})



#Удаление товара

class DeleteProductView(generic.DeleteView):
    template_name = 'CRUD/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Man_shop, id=person_id)


# def delete_product(request, id):
#     product_id = get_object_or_404(models.Man_shop, id=id)
#     product_id.delete()
#     return HttpResponse('Товар удален')


#Обновление товара
class UpdateProductView(generic.UpdateView):
    template_name = 'CRUD/update_product.html'
    form_class = forms.Man_shop_form
    success_url = '/'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Man_shop, id=person_id)

    def form_valid(self, form):
        return super(UpdateProductView, self).form_valid(form=form)



# def update_product(request,id):
#     product_id = get_object_or_404(models.Man_shop, id=id)
#     if request.method == 'POST':
#         form = forms.Man_shop_form(instance=product_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Товар успешно изменён')
#     else:
#         form = forms.Man_shop_form(instance=product_id)
#     context = {
#         'form': form,
#         'product_id': product_id
#     }
#     return render(request, 'CRUD/update_product.html', context)

class Search(generic.ListView):
    template_name = 'product/product.html'
    context_object_name = 'product'
    paginate_by = 5

    def get_queryset(self):
        return models.Man_shop.objects.filter(product_name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



