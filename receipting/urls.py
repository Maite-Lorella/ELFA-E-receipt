from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customer_list, name='customer-list'),
    path('customers/create/', views.create_customer, name='create-customer'),
    path('products/', views.product_list, name='product-list'),
    path('transactions/', views.transaction_list, name='transaction-list'),
    path('payments/', views.payment_list, name='payment-list'),
    path('receipts/', views.receipt_list, name='receipt-list'),
]