from django.urls import path
from . import views

urlpatterns = [

    path(
        "customers/",
        views.customer_list,
        name="customer_list"
    ),

    path(
        "customers/add/",
        views.add_customer,
        name="add_customer"
    ),

    path(
        "customers/edit/<int:id>/",
        views.edit_customer,
        name="edit_customer"
    ),

    path(
        "customers/delete/<int:id>/",
        views.delete_customer,
        name="delete_customer"
    ),

]