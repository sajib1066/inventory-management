from django.shortcuts import render

from store.models import Product, Supplier, Buyer, Order

def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_oder = Order.objects.count()
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_oder
    }
    return render(request, 'dashboard.html', context)