from django.urls import path
from .views import seller_portal, customer_portal

urlpatterns = [
    path('seller/', seller_portal, name='seller-portal'),
    path('customer/', customer_portal, name='customer-portal')
]
