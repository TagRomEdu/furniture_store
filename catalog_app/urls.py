from django.urls import path
from catalog_app.apps import CatalogAppConfig

from catalog_app.views import catalog, product

app_name = CatalogAppConfig.name

urlpatterns = [
    path('', catalog, name='index'),
    path('product/', product, name='product'),
]
