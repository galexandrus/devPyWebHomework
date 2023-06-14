from django.shortcuts import render

from django.views import View

from django.db.models import OuterRef, Subquery, ExpressionWrapper, DecimalField, Case, When, F
from django.utils import timezone
from .models import Product, Discount


class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ProductSingleView(View):
    def get(self, request, id):
        data = {
            1: {
                'name': 'Bell Pepper',
                'description': "Sweet color pepper",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-1.jpg',
            },
            2: {
                'name': 'Strawberry',
                'description': "Fragrant sweet strawberry",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-2.jpg',
            },
            3: {
                'name': 'Green Beans',
                'description': "Healthy delicious beans",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-3.jpg',
            },
            4: {
                'name': 'Purple Cabbage',
                'description': "Deep purple cabbage",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-4.jpg',
            },
            5: {
                'name': 'Tomato',
                'description': "Red and fragrant tomato",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-5.jpg',
            },
            6: {
                'name': 'Brocolli',
                'description': "Round and healthy brocolli",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-6.jpg',
            },
            7: {
                'name': 'Carrot',
                'description': "Red and tasty carrots",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-7.jpg',
            },
            8: {
                'name': 'Fruit Juice',
                'description': "Natural fruit juice",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-8.jpg',
            },
            9: {
                'name': 'Onion',
                'description': "Just onion",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-9.jpg',
            },
            10: {
                'name': 'Apple',
                'description': "Sweet red, green and yellow apples",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-10.jpg',
            },
            11: {
                'name': 'Garlic',
                'description': "Fresh and fragrant garlic",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-11.jpg',
            },
            12: {
                'name': 'Chilli',
                'description': "Spicy chilli",
                'price': 120.00,
                'rating': 5.0,
                'url': 'store/images/product-12.jpg',
            },
        }
        return render(request, 'store/product-single.html', context=data[id])


class ShopView(View):
    def get(self, request):
        # Request for all actual discounts
        discount_value = Case(
            When(
                discount_value_gte=0,
                discount_date_begin_lte=timezone.now(),
                discount_date_end_gte=timezone.now(),
                then=F('discount_value')
            ),
            default=0,
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        # Request for calculate price with discount
        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount_value')) / 100.0,
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        products = Product.objects.annotate(
            discount_value=discount_value,
            # Alternative way with subquery:
            # discount_value=Subquery(
            #     Discount.objects.filter(product_id=OuterRef('id').values('value'))
            # ),
            price_before=F('price'),
            price_after=price_with_discount,
        ).values('id', 'name', 'image', 'price_before', 'price_after', 'discount_value')

        return render(request, 'store/shop.html', {"data": products})

    # def get(self, request):
        # context = {
        #     'data': [
        #         {
        #             'name': 'Bell Pepper',
        #             'discount': 25,
        #             'price_before': 120.00,
        #             'price_after': 90.00,
        #             'id': 1,
        #             'url': 'store/images/product-1.jpg',
        #         },
        #         {
        #             'name': 'Strawberry',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 2,
        #             'url': 'store/images/product-2.jpg',
        #         },
        #         {
        #             'name': 'Green Beans',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 3,
        #             'url': 'store/images/product-3.jpg',
        #         },
        #         {
        #             'name': 'Purple Cabbage',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 4,
        #             'url': 'store/images/product-4.jpg',
        #         },
        #         {
        #             'name': 'Tomato',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 5,
        #             'url': 'store/images/product-5.jpg',
        #         },
        #         {
        #             'name': 'Brocolli',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 6,
        #             'url': 'store/images/product-6.jpg',
        #         },
        #         {
        #             'name': 'Carrot',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 7,
        #             'url': 'store/images/product-7.jpg',
        #         },
        #         {
        #             'name': 'Fruit Juice',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 8,
        #             'url': 'store/images/product-8.jpg',
        #         },
        #         {
        #             'name': 'Onion',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 9,
        #             'url': 'store/images/product-9.jpg',
        #         },
        #         {
        #             'name': 'Apple',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 10,
        #             'url': 'store/images/product-10.jpg',
        #         },
        #         {
        #             'name': 'Garlic',
        #             'discount': None,
        #             'price_before': 120.00,
        #             'price_after': 120.00,
        #             'id': 11,
        #             'url': 'store/images/product-11.jpg',
        #         },
        #         {
        #             'name': 'Chilli',
        #             'discount': 20,
        #             'price_before': 120.00,
        #             'price_after': 96.00,
        #             'id': 12,
        #             'url': 'store/images/product-12.jpg',
        #         },
        #     ]
        # }
        # return render(request, 'store/shop.html', context)
