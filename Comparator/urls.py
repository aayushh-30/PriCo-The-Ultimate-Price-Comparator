from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.test,name = "testing"),
    path("Search/",views.Search,name = "Searching")
]