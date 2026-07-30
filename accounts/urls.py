from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
path(
    "logout/",
    views.logout_user,
    name="logout"
),