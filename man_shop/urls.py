from django.urls import path
from man_shop import views




urlpatterns = [
    path('', views.product_view, name='product'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('product_detail/<int:id>/delete/', views.delete_product, name='delete_product'),
    path('product_detail/<int:id>/update/', views.update_product, name='update_product'),
    path('add-product/', views.create_product_view, name='create_product')
]
