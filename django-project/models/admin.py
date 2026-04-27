from django.contrib import admin
from django.db.models.fields.related import ForeignObjectRel
from djangoql.admin import DjangoQLSearchMixin
from .models import (
    Customer, Employee, Vehicle, Billing,
    Sales, ServiceData, WorkedOn, InventoryVehicle
)
from import_export.admin import ImportExportModelAdmin

def get_fields(model):
    return [
        field.name for field in model._meta.get_fields()
        if not isinstance(field, ForeignObjectRel)
    ]

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = get_fields(Customer)

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = get_fields(Employee)

@admin.register(Vehicle)
class VehicleAdmin(ImportExportModelAdmin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = get_fields(Vehicle)

@admin.register(Billing)
class BillingAdmin(ImportExportModelAdmin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = get_fields(Billing)

@admin.register(Sales)
class SalesAdmin(ImportExportModelAdmin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = get_fields(Sales)

@admin.register(ServiceData)
class ServiceDataAdmin(ImportExportModelAdmin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = get_fields(ServiceData)

@admin.register(WorkedOn)
class WorkedOnAdmin(ImportExportModelAdmin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = get_fields(WorkedOn)

@admin.register(InventoryVehicle)
class InventoryVehicleAdmin(ImportExportModelAdmin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = get_fields(InventoryVehicle)