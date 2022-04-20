from django.shortcuts import render

from phones.models import Phone


def show_catalog(request, sort):
    sot = request.GET.get('sort')
    template = 'catalog.html'
    context = {'phone': [list(Phone.objects.all())], 'sort': sot}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(title='slug')
    context = {'phone': phone}
    return render(request, template, context)
