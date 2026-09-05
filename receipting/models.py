from django.db import models
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True)
    logo = models.ImageField(
        upload_to='organization/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='staff_members'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    signature = models.ImageField(
        upload_to='signatures/',
        blank=True,
        null=True
    )
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return self.name
class Transaction(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='transactions'
    )
    reference_number = models.CharField(
        max_length=100,
        unique=True
    )
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    amount_paid = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    due_date = models.DateField(
        null=True,
        blank=True
    )
    transaction_date = models.DateTimeField(
        auto_now_add=True
    )
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.reference_number  
class TransactionItem(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='transaction_items'
    )
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return self.description
    
class Payment(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.PROTECT,
        related_name='payments'
    )
    payment_reference = models.CharField(
        max_length=100,
        unique=True
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    amount_in_words = models.CharField(max_length=255)
    payment_date = models.DateTimeField(
        auto_now_add=True
    )
    location = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return self.payment_reference
class Receipt(models.Model):
    payment = models.OneToOneField(
        Payment,
        on_delete=models.PROTECT,
        related_name='receipt'
    )
    staff = models.ForeignKey(
        Staff,
        on_delete=models.PROTECT,
        related_name='receipts'
    )
    receipt_number = models.CharField(
        max_length=100,
        unique=True
    )
    qr_code = models.CharField(max_length=500)
    issued_at = models.DateTimeField(
        auto_now_add=True
    )
    signature = models.ImageField(
        upload_to='receipt_signatures/',
        blank=True,
        null=True
    )
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.receipt_number