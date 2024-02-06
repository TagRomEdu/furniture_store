from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Каталог - Главная'
    }
    return render(request, 'catalog_app/catalog.html', context)


def product(request):
    context = {
        'title': 'Карточка товара'
    }
    return render(request, 'catalog_app/product.html', context)
