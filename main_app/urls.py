from django.urls import path
from main_app.apps import MainAppConfig

from main_app.views import about, index

app_name = MainAppConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
