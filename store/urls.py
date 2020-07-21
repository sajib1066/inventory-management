from django.urls import path

from .views import (
    create_supplier,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
]