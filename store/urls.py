from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_season,
    create_drop,
    create_product,

    SupplierListView,
    BuyerListView,
    SeasonListView,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
]