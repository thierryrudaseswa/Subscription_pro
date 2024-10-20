from django.contrib import admin
from django.urls import path, include  # Use include to reference your app's URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('subscriptions.urls')),  # Include your app's URLs
]
