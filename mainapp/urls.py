from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue_page'),
    path('cart/', CartView.as_view(), name='cart_page'),
    path('api/add-product', AddProduct.as_view(), name='add-product'),
    path('api/change-cart-product', ChangeCartProduct.as_view(), name='change-cart-product')
]