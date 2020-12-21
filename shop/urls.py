from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shopHome"),
    path("home", views.home, name="Home"),
    path("about", views.about, name="aboutus"),
    path("contact", views.contact, name="contactus"),
    path("products/<int:myid>", views.products, name="productViews"),
    path("search", views.search, name="search"),
    path("checkout", views.checkout, name="checkout"),
    path("tracker", views.tracker, name="Tracker"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
