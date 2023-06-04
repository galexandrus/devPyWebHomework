from django.shortcuts import render

from django.views import View
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        return render(request, 'login/index.html')
