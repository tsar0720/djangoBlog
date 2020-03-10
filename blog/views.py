from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import Category

# Create your views here.
# request - запрос response - ответ


class HomeView(View):
    """Домашняя страница"""
    def get(self, request):
        category_list = Category.objects.all()
        print(category_list)
        return render(request, "blog/home.html", {"categories": category_list})