# from django.contrib import admin

# # Register your models here.

# from django.contrib import admin
# from .models import Car, Customer, Rental

# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     list_display = ['make', 'model', 'year', 'color', 'license_plate', 'mileage', 'available']
#     list_filter = ['make', 'model', 'year', 'color', 'available']
#     search_fields = ['make', 'model', 'license_plate']

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'email', 'phone']
#     search_fields = ['first_name', 'last_name', 'email']

# @admin.register(Rental)
# class RentalAdmin(admin.ModelAdmin):
#     list_display = ['car', 'customer', 'rental_date', 'return_date']
#     list_filter = ['car', 'customer', 'rental_date', 'return_date']
#     search_fields = ['car__make', 'car__model', 'customer__first_name', 'customer__last_name']
#     # rental/admin.py
from django.contrib import admin
from .models import Car, Customer, Rental

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'color', 'license_plate', 'mileage', 'available')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')

class RentalAdmin(admin.ModelAdmin):
    list_display = ('car', 'customer', 'rental_date', 'return_date')

admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rental, RentalAdmin)

