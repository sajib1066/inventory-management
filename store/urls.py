from django.urls import path

from .views import (
    create_supplier,
    SupplierListView,
    create_buyer,
    BuyerListView,
    create_season,
    create_drop
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
]