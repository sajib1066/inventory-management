from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_season,
    create_drop,
    create_product,
    create_order,

    SupplierListView,
    BuyerListView,
    SeasonListView,
    DropListView,
    ProductListView,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
]