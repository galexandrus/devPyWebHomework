from django.shortcuts import render
from datetime import datetime

from django.views import View
from django.http import HttpResponse

import random


class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')


class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class Hello(View):
    def get(self, request):
        html = "<h1>Say hello to my little friend!</h1>"
        return HttpResponse(html)


class RandomNumber(View):
    def get(self, request):
        html = f"{random.randrange(0, 101)}"
        return HttpResponse(html)
