from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import *
import re


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
    if request.method == "POST":
        # check if the prayer has a parent
        if request.POST.get("parent"):
            parent = Prayer.objects.get(id=int(request.POST.get("parent")))
        else:
            parent = None

        new_prayer = Prayer(name=request.POST.get('name'), publish=int(request.POST.get('publish')), parent=parent)
        new_prayer.save()
        # check if the post request contains category
        if request.POST.get("category"):
            category_list = request.POST.getlist("category")
            for category in category_list:
                new_prayer.category_set.add(int(category))
        # check if the post request contains text area
        if request.POST.get("phrases"):
            # phrase count
            count = 0
            # split the text area
            phrase_list = request.POST.get("phrases").split("\n")
            for phrase in phrase_list:
                count += 1
                explanation = re.findall("#.*#", phrase)
                quran = re.findall("[$].*[$]", phrase)
                # checking the phrase type
                if explanation:
                    for sharp in explanation:
                        removed_sharp = sharp.replace('#', '')
                        Phrase.objects.create(text=removed_sharp, order=f"{new_prayer.id},{count}", type=1,
                                              prayer=new_prayer)
                elif quran:
                    for dollar in quran:
                        removed_dollar = dollar.replace('$', '')
                        Phrase.objects.create(text=removed_dollar, order=f"{new_prayer.id},{count}", type=3,
                                              prayer=new_prayer)
                # do not add empty rows
                elif phrase != "":
                    Phrase.objects.create(text=phrase, order=f"{new_prayer.id},{count}", type=2, prayer=new_prayer)

        return render(request, "html/edit_prayer_page.html", {"Prayer": Prayer.objects.get(id=new_prayer.id)})
    return render(request, "html/prayer_list.html", {"Prayer": Prayer.objects.all()})


@csrf_protect
def create_category(request):
    if request.method == "POST":
        print("asdfasdfasdfasdfsdaf")
        if request.POST.get("parent"):
            parent = Category.objects.get(id=int(request.POST.get("parent")))
        else:
            parent = None

        new_category = Category(title=request.POST.get('name'), publish=int(request.POST.get('publish')),
                                index=int(request.POST.get('index')), parent=parent)
        new_category.save()
        return render(request, "html/edit_category_page.html", {"Category": Category.objects.get(id=new_category.id)})
    return render(request, "html/category_list.html", {"Category": Category.objects.all()})


def edit_prayer_page(request, id):
    return render(request, 'html/edit_prayer_page.html', {"Prayer": Prayer.objects.get(id=id)})


def edit_category_page(request, id):
    return render(request, 'html/edit_category_page.html', {"Category": Category.objects.get(id=id)})
