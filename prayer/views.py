from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import *


@csrf_protect
# Create your views here.
def first_page(request):
    queryset = Category.objects.all()
    return render(request, "html/create_category.html", {"Category": queryset})


def create_prayer_page(request):
    queryset = Category.objects.all()
    return render(request, "html/create_prayer.html", {"Category": queryset, "Prayer": Prayer.objects.all()})


def create_category_page(request):
    queryset = Category.objects.all()
    return render(request, "html/create_category.html", {"Category": queryset})


@csrf_protect
def create_prayer(request):
    prayer_name = request.POST.get('name')
    print(request.POST)
    # Prayer.objects.create()
    return render(request, "html/prayer_list.html", {"Prayer": Prayer.objects.all()})


@csrf_protect
def create_category(request):
    prayer_name = request.POST.get('name')
    print(request.POST)
    # Prayer.objects.create()
    return render(request, "html/category_list.html", {"Category": Category.objects.all()})
