from django.urls import path
from .views import CartView, ProductSingleView, ShopView, CartViewSet, WishlistView, WishlistViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'wishlist', WishlistViewSet)

app_name = 'store'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductSingleView.as_view(), name='product'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]
