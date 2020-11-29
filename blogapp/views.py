from django.shortcuts import render, get_object_or_404
from .models import Author, Article, Category


def home(request):
    post = Article.objects.all()
    context = {
        "post": post
    }
    return render(request, 'index.html', context)


def getauthor(request, name):
    return render(request, 'profile.html')


def getsingle(request, id):
    post = get_object_or_404(Article, pk=id)
    context = {
        "post": post
    }
    return render(request, 'single.html', context)


def getcategory(request, name):
    cat = get_object_or_404(Category, name=name)
    post = Article.objects.filter(category=cat.id)
    return render(request, 'category.html', {"post": post})
