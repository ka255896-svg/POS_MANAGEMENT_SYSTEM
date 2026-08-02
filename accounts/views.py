from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from products.models import Product
from customers.models import Customer
from sales.models import Sale

from django.db.models import Sum
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("dashboard")

        else:
            return render(
                request,
                "login.html",
                {
                    "error": "Invalid username or password"
                }
            )

    return render(request, "login.html")

@login_required
def dashboard(request):

    today = timezone.now().date()


    # ==========================
    # General Statistics
    # ==========================

    total_products = Product.objects.count()

    total_customers = Customer.objects.count()

    total_sales = Sale.objects.count()


    total_revenue = (
        Sale.objects.aggregate(
            total=Sum("total_price")
        )["total"] or 0
    )



    # ==========================
    # Today's Sales
    # ==========================

    today_sales = Sale.objects.filter(
        sale_date__date=today
    )


    today_revenue = (
        today_sales.aggregate(
            total=Sum("total_price")
        )["total"] or 0
    )


    today_profit = (
        today_sales.aggregate(
            total=Sum("profit")
        )["total"] or 0
    )



    # ==========================
    # Low Stock
    # ==========================

    low_stock = Product.objects.filter(
        quantity__lt=5
    )



    # ==========================
    # Recent Transactions
    # ==========================

    recent_sales = (
        Sale.objects
        .select_related(
            "customer",
            "product"
        )
        .order_by("-sale_date")[:5]
    )



    # ==========================
    # Sales Chart
    # ==========================

    sales_data = (
        Sale.objects
        .values("sale_date__date")
        .annotate(
            total=Sum("total_price")
        )
        .order_by("sale_date__date")
    )


    sales_dates = [
        str(item["sale_date__date"])
        for item in sales_data
    ]


    sales_totals = [
        float(item["total"])
        for item in sales_data
    ]



    # ==========================
    # Best Selling Products
    # ==========================

    top_products = (
        Sale.objects
        .values(
            "product__product_name"
        )
        .annotate(
            total_quantity=Sum("quantity")
        )
        .order_by("-total_quantity")[:5]
    )


    product_names = [
        item["product__product_name"]
        for item in top_products
    ]


    product_quantities = [
        item["total_quantity"]
        for item in top_products
    ]



    context = {

        "total_products": total_products,

        "total_customers": total_customers,

        "total_sales": total_sales,

        "total_revenue": total_revenue,


        "today_revenue": today_revenue,

        "today_profit": today_profit,


        "low_stock": low_stock.count(),


        "recent_sales": recent_sales,



        "sales_dates": json.dumps(
            sales_dates
        ),

        "sales_totals": json.dumps(
            sales_totals
        ),


        "product_names": json.dumps(
            product_names
        ),

        "product_quantities": json.dumps(
            product_quantities
        ),

    }


    return render(
        request,
        "dashboard.html",
        context
    )
def logout_user(request):

    logout(request)

    return redirect("login")