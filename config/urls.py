from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/login/")),
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("products.urls")),
    path("", include("sales.urls")),
    path("", include("customers.urls")),
]

