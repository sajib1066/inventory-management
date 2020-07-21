from django.urls import path

from .views import (
    create_supplier,
    SupplierListView,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
]