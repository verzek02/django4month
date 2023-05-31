from django.urls import path
from man_shop import views




urlpatterns = [
    path('', views.PersonView.as_view(), name='product'),
    path('product_detail/<int:id>/', views.PersonDetailView.as_view(), name='product_detail'),
    path('product_detail/<int:id>/delete/', views.DeleteProductView.as_view(), name='delete_product'),
    path('product_detail/<int:id>/update/', views.UpdateProductView.as_view(), name='update_product'),
    path('add-product/', views.CreateProductView.as_view(), name='create_product'),
    path('search/', views.Search.as_view(), name='search'),
]
