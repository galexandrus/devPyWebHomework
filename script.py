import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_store.settings')
django.setup()

from store.models import Product, Category


if __name__ == '__main__':
    category = Category.objects.get(name='Vegetables')
    obj = Product(
        name='Carrot',
        description='Red and tasty carrots',
        price=120,
        image='static/products/product-7.jpg',
        category=category
    )
    obj.save()

    obj = Product.objects.create(
        name='Fruit Juice',
        description='Natural fruit juice',
        price=120,
        image='static/products/product-8.jpg',
        category=Category.objects.get(name='Juice')
    )

    data = (
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
        # {
        #     'name': 'Chilli',
        #     'price': 120,
        #     'description': 'Spicy chilli',
        #     'image': 'static/products/product-12.jpg',
        #     'category': 'Vegetables',
        # },
    )

    categ = {
        'Fruits': Category.objects.get(name='Fruits'),
        'Vegetables': Category.objects.get(name='Vegetables'),
    }

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
