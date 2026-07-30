from django.urls import path
from . import views


urlpatterns = [

    path(
        "products/",
        views.product_list,
        name="product_list"
    ),

    path(
        "products/add/",
        views.add_product,
        name="add_product"
    ),

    path(
        "products/edit/<int:id>/",
        views.edit_product,
        name="edit_product"
    ),

    path(
        "products/delete/<int:id>/",
        views.delete_product,
        name="delete_product"
    ),


    path(
        "categories/",
        views.category_list,
        name="category_list"
    ),

    path(
        "categories/add/",
        views.add_category,
        name="add_category"
    ),

    path(
        "categories/delete/<int:id>/",
        views.delete_category,
        name="delete_category"
    ),

]