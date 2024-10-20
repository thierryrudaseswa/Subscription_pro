from django.urls import path
from .views import home, customer_list, subscription_list, create_customer, create_subscription

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('customer_list/', customer_list, name='customer_list'),  # Customer list page
    path('subscription_list/', subscription_list, name='subscription_list'),  # Subscription list page
    path('create_customer/', create_customer, name='create_customer'),  # Endpoint to create customer
    path('create_subscription/', create_subscription, name='create_subscription'),  # Endpoint to create subscription
]
