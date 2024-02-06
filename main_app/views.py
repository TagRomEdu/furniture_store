from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели'
    }
    return render(request, 'main_app/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'Мы ооочень крутые!',
        'pohvala': 'Наша мебель служит веками (гарантия не предоставляется).'
    }
    return render(request, 'main_app/about.html', context)
