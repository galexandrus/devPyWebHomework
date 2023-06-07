from django.shortcuts import render

from django.views import View

from django.db.models import OuterRef, Subquery, F, ExpressionWrapper, DecimalField, Case, When
from django.utils import timezone
from .models import Product, Discount


class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ProductSingleView(View):
    def get(self, request):
        return render(request, 'store/product-single.html')


class ShopView(View):
    def get(self, request):
        discout_value = Case(When(discount__value__get=0,
                                  discount__date__begin__lte=timezone.now()),
                             discount__date__end__gte=timezone.now(),
                             then=F('discount__value'),
                             default=0,
                             output_field=DecimalField(max_digits=10, decimal_places=2)
                             )
        price_with_discount = ExpressionWrapper(
            F('prcie') * (100.0 - F('discount_value')) / 100.0,
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        products = Product.objects.annotate(
            discout_value=discout_value,
            price_before=F('price'),
            price_after=price_with_discount,
        ).values('id', 'name', 'image', 'price_before', 'price_after', 'discount_value')

        return render(request, 'store/shop.html', {'data': products})


class ProductView(View):
    def get(self, request, id):
        data = Product.objects.get(id=id)
        return render(
            request,
            'store/product-single.html',
            context={
                'name': data.name,
                'description': data.description,
                'price': data.price,
            }
        )
