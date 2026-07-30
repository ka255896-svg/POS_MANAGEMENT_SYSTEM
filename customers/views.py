from django.shortcuts import render, redirect
from .models import Customer
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def customer_list(request):

    search = request.GET.get("search", "")

    customers = Customer.objects.all()

    if search:
        customers = Customer.objects.filter(
            Q(full_name__icontains=search) |
            Q(phone__icontains=search) |
            Q(email__icontains=search)
        )

    return render(
        request,
        "customer_list.html",
        {
            "customers": customers,
            "search": search
        }
    )


def add_customer(request):

    if request.method == "POST":

        Customer.objects.create(
            full_name=request.POST["full_name"],
            phone=request.POST["phone"],
            email=request.POST["email"],
            address=request.POST["address"]
        )

        return redirect("customer_list")

    return render(request, "add_customer.html")


def edit_customer(request, id):

    customer = Customer.objects.get(id=id)

    if request.method == "POST":

        customer.full_name = request.POST["full_name"]
        customer.phone = request.POST["phone"]
        customer.email = request.POST["email"]
        customer.address = request.POST["address"]

        customer.save()

        return redirect("customer_list")

    return render(
        request,
        "edit_customer.html",
        {"customer": customer}
    )


def delete_customer(request, id):

    customer = Customer.objects.get(id=id)

    customer.delete()

    return redirect("customer_list")