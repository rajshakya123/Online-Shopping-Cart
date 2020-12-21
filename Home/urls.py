from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("logout", views.handlelogout, name="handlelogout"),
    path("basic", views.basic, name="basic"),
    path("login", views.handlelogin, name="handlelogin"),
    path("", views.index, name="index")

]
