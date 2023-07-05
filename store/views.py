from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import OuterRef, Subquery, ExpressionWrapper, DecimalField, Case, When, F
from django.utils import timezone
from .models import Product, Discount, Cart, Wishlist
from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer, WishlistSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class WishlistView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = Wishlist.objects.filter(user=request.user)
            return render(request, 'store/wishlist.html', {"data": data})
        return redirect('login:login')


class CartViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer
  permission_classes = (IsAuthenticated,)

  def get_queryset(self):
      return self.queryset.filter(user=self.request.user)

  def create(self, request, *args, **kwargs):
      ## Можно записать так, для получения товара (проверка что он уже есть в корзине)
      # cart_items = Cart.objects.filter(user=request.user,
      #                                  product__id=request.data.get('product'))
      # Или можно так, так как мы переопределили метод get_queryset
      cart_items = self.get_queryset().filter(product__id=request.data.get('product'))
      # request API передаёт параметры по названиям полей в БД, поэтому ловим product
      if cart_items:  # Если продукт уже есть в корзине
          cart_item = cart_items[0]
          if request.data.get('quantity'):  # Если в запросе передан параметр quantity,
              # то добавляем значение к значению в БД
              cart_item.quantity += int(request.data.get('quantity'))
          else:  # Иначе просто добавляем значение по умолчению 1
              cart_item.quantity += 1
      else:  # Если продукта ещё нет в корзине
          product = get_object_or_404(Product, id=request.data.get('product'))  # Получаем продукт и
          # проверяем что он вообще существует, если его нет то выйдет ошибка 404
          if request.data.get('quantity'):  # Если передаём точное количество продукта, то передаём его
              cart_item = Cart(user=request.user, product=product, quantity=request.data.get('quantity'))
          else:  # Иначе создаём объект по умолчанию (quantity по умолчанию = 1, так прописали в моделях)
              cart_item = Cart(user=request.user, product=product)
      cart_item.save()  # Сохранили объект в БД
      return response.Response({'message': 'Product added to cart'})  # Вернули ответ, что всё прошло успешно

  def update(self, request, *args, **kwargs):
      # Для удобства в kwargs передаётся id строки для изменения в БД, под параметром pk
      cart_item = get_object_or_404(Cart, id=kwargs['pk'])
      if request.data.get('quantity'):
          cart_item.quantity = request.data['quantity']
      if request.data.get('product'):
          product = get_object_or_404(Product, id=request.data['product'])
          cart_item.product = product
      cart_item.save()
      return response.Response({'message': 'Product change to cart'}, status=201)

  def destroy(self, request, *args, **kwargs):
      # В этот раз напишем примерно так как это делает фреймфорк самостоятельно
      cart_item = self.get_queryset().get(id=kwargs['pk'])
      cart_item.delete()
      return response.Response({'message': 'Product delete from cart'}, status=201)


class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ProductSingleView(View):
    def get(self, request, id):
        data = Product.objects.get(id=id)
        return render(request,
                      'store/product-single.html',
                      context={
                          'name': data.name,
                          'description': data.description,
                          'price': data.price,
                          'rating': 5.0,
                          'url': data.image.url,
                      })

        # data = {
        #     1: {
        #         'name': 'Bell Pepper',
        #         'description': "Sweet color pepper",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-1.jpg',
        #     },
        #     2: {
        #         'name': 'Strawberry',
        #         'description': "Fragrant sweet strawberry",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-2.jpg',
        #     },
        #     3: {
        #         'name': 'Green Beans',
        #         'description': "Healthy delicious beans",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-3.jpg',
        #     },
        #     4: {
        #         'name': 'Purple Cabbage',
        #         'description': "Deep purple cabbage",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-4.jpg',
        #     },
        #     5: {
        #         'name': 'Tomato',
        #         'description': "Red and fragrant tomato",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-5.jpg',
        #     },
        #     6: {
        #         'name': 'Brocolli',
        #         'description': "Round and healthy brocolli",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-6.jpg',
        #     },
        #     7: {
        #         'name': 'Carrot',
        #         'description': "Red and tasty carrots",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-7.jpg',
        #     },
        #     8: {
        #         'name': 'Fruit Juice',
        #         'description': "Natural fruit juice",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-8.jpg',
        #     },
        #     9: {
        #         'name': 'Onion',
        #         'description': "Just onion",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-9.jpg',
        #     },
        #     10: {
        #         'name': 'Apple',
        #         'description': "Sweet red, green and yellow apples",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-10.jpg',
        #     },
        #     11: {
        #         'name': 'Garlic',
        #         'description': "Fresh and fragrant garlic",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-11.jpg',
        #     },
        #     12: {
        #         'name': 'Chilli',
        #         'description': "Spicy chilli",
        #         'price': 120.00,
        #         'rating': 5.0,
        #         'url': 'store/images/product-12.jpg',
        #     },
        # }
        # return render(request, 'store/product-single.html', context=data[id])


class ShopView(View):
    def get(self, request):
        # Request for all actual discounts
        discount_value = Case(
            When(discount__value__gte=0,
                 discount__date_begin__lte=timezone.now(),
                 discount__date_end__gte=timezone.now(),
                 then=F('discount__value')
                 ),
            default=0,
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        # Request for calculate price with discount
        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount__value')) / 100.0,
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
