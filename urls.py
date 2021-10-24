from django.urls import path
from Images_app import views

urlpatterns = [
    path("",views.base , name = "Display")
]