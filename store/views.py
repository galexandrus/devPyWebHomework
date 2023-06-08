from django.shortcuts import render

from django.views import View


class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ProductSingleView(View):
    def get(self, request):
        return render(request, 'store/product-single.html')


class ShopView(View):
    def get(self, request):
        context = {
            'data': [
                {
                    'name': 'Bell Pepper',
                    'discount': 25,
                    'price_before': 120.00,
                    'price_after': 95.00,
                    'url': 'store/images/product-1.jpg',
                },
                {
                    'name': 'Strawberry',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-2.jpg',
                },
                {
                    'name': 'Green Beans',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-3.jpg',
                },
                {
                    'name': 'Purple Cabbage',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-4.jpg',
                },
                {
                    'name': 'Tomato',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-5.jpg',
                },
                {
                    'name': 'Brocolli',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-6.jpg',
                },
                {
                    'name': 'Carrots',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-7.jpg',
                },
                {
                    'name': 'Fruit Juice',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-8.jpg',
                },
                {
                    'name': 'Onion',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-9.jpg',
                },
                {
                    'name': 'Apple',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-10.jpg',
                },
                {
                    'name': 'Garlic',
                    'discount': 0,
                    'price_before': 120.00,
                    'price_after': 120.00,
                    'url': 'store/images/product-11.jpg',
                },
                {
                    'name': 'Chilli',
                    'discount': 20,
                    'price_before': 120.00,
                    'price_after': 100.00,
                    'url': 'store/images/product-12.jpg',
                },
            ]
        }
        return render(request, 'store/shop.html', context)
