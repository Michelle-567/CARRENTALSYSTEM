# from django.contrib import admin
# from .models import Car, Customer, Rental

# class CarAdmin(admin.ModelAdmin):
#     list_display = ('make', 'model', 'year', 'color', 'license_plate', 'mileage', 'available')

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'phone')

# class RentalAdmin(admin.ModelAdmin):
#     list_display = ('car', 'customer', 'rental_date', 'return_date')

# admin.site.register(Car, CarAdmin)
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Rental, RentalAdmin)
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


