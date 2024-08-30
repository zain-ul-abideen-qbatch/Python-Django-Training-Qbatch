from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

handler404 = "students.views.custom_404_view"

urlpatterns = [
 
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup_view, name='signup'),
    path('', views.Home, name='home'),

]
