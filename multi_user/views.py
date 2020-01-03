from django.shortcuts import render


# Create your views here.

def seller_portal(request):
    return render(request, 'django_users/seller.html', {'title': 'Seller portal'})


def customer_portal(request):
    return render(request, 'django_users/customer.html', {'title': 'Seller portal'})
