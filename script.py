import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_store.settings')
django.setup()

from store.models import Product, Category


if __name__ == '__main__':
    data1 = (
        {
            'name': 'Bell Pepper',
            'price': 120,
            'description': 'Sweet color pepper',
            'image': 'static/products/product-1.jpg',
            'category': 'Vegetables',
        },
        {
            'name': 'Strawberry',
            'price': 120,
            'description': 'Fragrant sweet strawberry',
            'image': 'static/products/product-2.jpg',
            'category': 'Fruits',
        },
        {
            'name': 'Green Beans',
            'price': 120,
            'description': 'Healthy delicious beans',
            'image': 'static/products/product-3.jpg',
            'category': 'Vegetables',
        },
        {
            'name': 'Purple Cabbage',
            'price': 120,
            'description': 'Deep purple cabbage',
            'image': 'static/products/product-4.jpg',
            'category': 'Vegetables',
        },
        {
            'name': 'Tomato',
            'price': 120,
            'description': 'Red and fragrant tomato',
            'image': 'static/products/product-5.jpg',
            'category': 'Vegetables',
        },
        {
            'name': 'Brocolli',
            'price': 120,
            'description': 'Round and healthy brocolli',
            'image': 'static/products/product-6.jpg',
            'category': 'Vegetables',
        },
    )

    # category = Category.objects.get(name='Vegetables')
    # obj = Product(
    #     name='Carrot',
    #     description='Red and tasty carrots',
    #     price=120,
    #     image='static/products/product-7.jpg',
    #     category=category
    # )
    # obj.save()
    #
    # obj = Product.objects.create(
    #     name='Fruit Juice',
    #     description='Natural fruit juice',
    #     price=120,
    #     image='static/products/product-8.jpg',
    #     category=Category.objects.get(name='Juice')
    # )

    data2 = (
        {
            'name': 'Carrot',
            'price': 120,
            'description': 'Red and tasty carrots',
            'image': 'static/products/product-7.jpg',
            'category': 'Vegetables',
        },
        {
            'name': 'Fruit Juice',
            'price': 120,
            'description': 'Natural fruit juice',
            'image': 'static/products/product-8.jpg',
            'category': 'Juice',
        },
        {
            'name': 'Onion',
            'price': 120,
            'description': 'Just onion',
            'image': 'static/products/product-9.jpg',
            'category': 'Vegetables',
        },
        {
            'name': 'Apple',
            'price': 120,
            'description': 'Sweet red, green and yellow apples',
            'image': 'static/products/product-10.jpg',
            'category': 'Fruits',
        },
        {
            'name': 'Garlic',
            'price': 120,
            'description': 'Fresh and fragrant garlic',
            'image': 'static/products/product-11.jpg',
            'category': 'Vegetables',
        },
        {
            'name': 'Chilli',
            'price': 120,
            'description': 'Spicy chilli',
            'image': 'static/products/product-12.jpg',
            'category': 'Vegetables',
        },
    )

    categ = {
        'Fruits': Category.objects.get(name='Fruits'),
        'Vegetables': Category.objects.get(name='Vegetables'),
        'Juice': Category.objects.get(name='Juice'),
        'Dried': Category.objects.get(name='Dried'),
    }

    data = data1 + data2

    objects_to_create = [
        Product(
            name=val['name'],
            description=val['description'],
            price=val['price'],
            image=val['image'],
            category=categ[val['category']]
        ) for val in data
    ]

    Product.objects.bulk_create(objects_to_create)
