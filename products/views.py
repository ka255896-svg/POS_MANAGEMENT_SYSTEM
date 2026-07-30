from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Product, Category


# ==========================
# CATEGORY LIST
# ==========================

def category_list(request):

    categories = Category.objects.all()

    return render(
        request,
        "category_list.html",
        {
            "categories": categories
        }
    )


# ==========================
# ADD CATEGORY
# ==========================

def add_category(request):

    if request.method == "POST":

        name = request.POST["name"]

        Category.objects.create(
            name=name
        )

        return redirect("category_list")


    return render(
        request,
        "add_category.html"
    )


# ==========================
# DELETE CATEGORY
# ==========================

def delete_category(request, id):

    category = get_object_or_404(
        Category,
        id=id
    )

    category.delete()

    return redirect("category_list")



# ==========================
# PRODUCT LIST + SEARCH + PROFIT
# ==========================

def product_list(request):

    search = request.GET.get(
        "search",
        ""
    )


    products = Product.objects.all()


    if search:

        products = Product.objects.filter(

            Q(product_name__icontains=search) |

            Q(category__name__icontains=search)

        )


    # Calculate profit

    for product in products:

        if product.cost_price is not None:

            product.profit = (
                product.price -
                product.cost_price
            )

        else:

            product.profit = 0



    return render(

        request,

        "product_list.html",

        {
            "products": products,
            "search": search
        }

    )



# ==========================
# ADD PRODUCT
# ==========================

def add_product(request):

    categories = Category.objects.all()


    if request.method == "POST":


        product_name = request.POST["product_name"]

        category_id = request.POST["category"]

        cost_price = request.POST["cost_price"]

        price = request.POST["price"]

        quantity = request.POST["quantity"]



        category = get_object_or_404(
            Category,
            id=category_id
        )



        Product.objects.create(

            product_name=product_name,

            category=category,

            cost_price=cost_price,

            price=price,

            quantity=quantity

        )


        return redirect(
            "product_list"
        )



    return render(

        request,

        "add_product.html",

        {
            "categories": categories
        }

    )



# ==========================
# EDIT PRODUCT
# ==========================

def edit_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )


    categories = Category.objects.all()



    if request.method == "POST":


        product.product_name = request.POST["product_name"]


        category_id = request.POST["category"]


        product.category = get_object_or_404(

            Category,

            id=category_id

        )


        product.cost_price = request.POST["cost_price"]


        product.price = request.POST["price"]


        product.quantity = request.POST["quantity"]



        product.save()



        return redirect(
            "product_list"
        )



    return render(

        request,

        "edit_product.html",

        {
            "product": product,
            "categories": categories
        }

    )



# ==========================
# DELETE PRODUCT
# ==========================

def delete_product(request, id):

    product = get_object_or_404(

        Product,

        id=id

    )


    product.delete()


    return redirect(
        "product_list"
    )