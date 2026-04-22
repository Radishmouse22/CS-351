from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=60)
    phoneNumber = models.CharField(max_length=10)

    class CustomerType(models.TextChoices):
        PURCHASE = 'Purchase',
        SERVICE = 'Service',
        VISIT = 'Visit',

    customerType = models.CharField(
        max_length=8,
        choices=CustomerType.choices,
        default=CustomerType.SERVICE,
    )