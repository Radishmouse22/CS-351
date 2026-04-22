from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phoneNumber', 'customerType')
