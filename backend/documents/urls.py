from django.urls import path
from . import views 

urlpatterns = [
    path('upload', views.upload_document ,name='upload_file'),
    #path('retrieve', views.retrieve_relevant, name='retrieve_relevant'), 
]
