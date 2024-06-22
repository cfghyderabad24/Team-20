from django.urls import path
from .import views

urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome"),
    path("adminlogout",views.logout,name="adminlogout"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("farmerhome",views.farmerhome,name="farmerhome"),
    path("farmerlogout",views.farmerlogout,name="farmerlogout"),
    path("checkfarmerlogin", views.checkfarmerlogin, name="checkfarmerlogin"),
path("farmerlogin", views.farmerlogin, name="farmerlogin"),
    path("login", views.login, name="login"),

]
