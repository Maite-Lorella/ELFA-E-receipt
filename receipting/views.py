from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .models import Customer

def home(request):
    return HttpResponse("Welcome to the ELFA Cameroon E-Receipting System")


def customer_list(request):
    customers = Customer.objects.all()

    response = "Customers:<br>"

    for customer in customers:
        response += f"{customer.full_name} - {customer.phone}<br>"

    return HttpResponse(response)

def create_customer(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")

        Customer.objects.create(
            full_name=full_name,
            phone=phone,
            email=email,
            address=address
        )

        return HttpResponse("Customer created successfully!")

    return render(
        request,
        "receipting/create_customer.html"
    )

def product_list(request):
    return HttpResponse("Product list")


def transaction_list(request):
    return HttpResponse("Transaction list")


def payment_list(request):
    return HttpResponse("Payment list")


def receipt_list(request):
    return HttpResponse("Receipt list")