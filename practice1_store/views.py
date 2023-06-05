from django.shortcuts import render

from django.views import View


class CartView(View):
    def get(self, request):
        return render(request, 'practice1_store/cart.html')


class ProductSingleView(View):
    def get(self, request):
        return render(request, 'practice1_store/product-single.html')


class ShopView(View):
    def get(self, request):
        return render(request, 'practice1_store/shop.html')
