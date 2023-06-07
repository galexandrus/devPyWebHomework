import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'test_store.settings')

django.setup()


from store.models import Product, Category

if __name__ == '__main__':
    category = Category.objects.get(name='Vegetables')
    obj = Product(name='Carrots', description='Fresh tasty carrots', price=120,
                  image='static/products/product-7.jpg',
                  category=category)

    obj.save()

    obj = Product.objects.create(name='Fruit Juice',
                                 description='Fruit Juice',
                                 price=120,
                                 image='static/products/product-8.jpg',
                                 category=Category.objects.get(name='Juice'))

    data = ({'name': 'Onion',
             'price': 120.00,
             'description': "Лук",
             'image': 'static/products/product-9.jpg',
             'category': 'Vegetables'},
            {'name': 'Apple',
             'price': 120.00,
             'description': "Яблоко",
             'image': 'static/products/product-10.jpg',
             'category': 'Fruits'},
            {'name': 'Garlic',
             'price': 120.00,
             'description': "Чеснок",
             'image': 'static/products/product-11.jpg',
             'category': 'Vegetables'},
            )

    # data = (
    #     {'name': 'Onion',
    #      'discount': 30,
    #      'description': 'Onion',
    #      'price': 120.00,
    #      # 'price_before': 120.00,
    #      # 'price_after': 80.00,
    #      'category': 'Vegetables',
    #      'id': 9,
    #      'url': 'store/images/product-9.jpg'},
    #     {'name': 'Apple',
    #      'discount': None,
    #      'description': 'Apple',
    #      'price': 120.00,
    #      # 'price_before': 120.00,
    #      'category': 'Fruits',
    #      'id': 10,
    #      'url': 'store/images/product-10.jpg'},
    #     {'name': 'Garlic',
    #      'discount': None,
    #      'description': 'Garlic',
    #      'price': 120.00,
    #      # 'price_before': 120.00,
    #      'category': 'Vegetables',
    #      'id': 11,
    #      'url': 'store/images/product-11.jpg'},
    #     {'name': 'Chilli',
    #      'discount': None,
    #      'description': 'Chilli',
    #      'price': 120.00,
    #      # 'price_before': 120.00,
    #      'category': 'Vegetables',
    #      'id': 12,
    #      'url': 'store/images/product-12.jpg'}
    # )

    categ = {
        'Fruits': Category.objects.get(name='Fruits'),
        'Vegetables': Category.objects.get(name='Vegetables'),
    }

    objects_to_create = [
        Product(name=val['name'],
                description=val['description'],
                price=val['price'],
                image=val['image'],
                category=categ[val['category']]) for val in data
    ]

    Product.objects.bulk_create(objects_to_create)
