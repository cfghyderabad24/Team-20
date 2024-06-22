from django.urls import path
from .import views

urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome"),
    path("adminlogout",views.logout,name="adminlogout"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("adminchangepwd", views.adminchangepwd, name="adminchangepwd"),
    path("adminupdatepwd", views.adminupdatepwd, name="adminupdatepwd"),
    path("login", views.login, name="login"),




]
