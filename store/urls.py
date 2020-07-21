from django.urls import path

from .views import (
    create_supplier,
    SupplierListView,
    create_buyer,
    BuyerListView
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
]