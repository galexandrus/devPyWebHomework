from django.urls import path

from .views import CartView, ProductSingleView, ShopView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('product-single/', ProductSingleView.as_view()),
    path('shop/', ShopView.as_view()),
]
