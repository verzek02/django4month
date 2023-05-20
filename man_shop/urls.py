from django.urls import path
from man_shop import views


urlpatterns = [
    path('', views.product_view, name='product'),
    path('product_detail/<int:id>/', views.product_deatil, name='product_detail')
]


