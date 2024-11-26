from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('documents.urls')),  # Include the URLs for the 'documents' app
]