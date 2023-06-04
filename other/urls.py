from django.urls import path

from .views import CurrentDateView, Hello, RandomNumber, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('hello/', Hello.as_view()),
    path('random_number/', RandomNumber.as_view()),
]
