from django.urls import path
from . import views

urlpatterns = [

    path(
        "sales/",
        views.sales_page,
        name="sales_page"
    ),

    path(
        "sales/history/",
        views.sales_history,
        name="sales_history"
    ),

    path(
    "receipt/<int:sale_id>/",
    views.receipt,
    name="receipt"
    ),
   path(
    "reports/",
    views.reports,
    name="reports"
   ),
  path(
    "sales/pdf/",
    views.sales_pdf,
    name="sales_pdf"
   ), 
   path(
    "sales/excel/",
    views.sales_excel,
    name="sales_excel",
   ),
]