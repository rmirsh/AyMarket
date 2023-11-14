from django.shortcuts import render

from aymarket.item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })


def contact(request):
    return render(request, 'core/contact.html')
