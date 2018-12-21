from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from webapp.models import Employee, Food, Order, OrderFoods

class EmployeeInLine(admin.StackedInline):
    model = Employee
    fields = ['phone']

class EmployeeAdmin(UserAdmin):
    inlines = [EmployeeInLine]

class OrderFoodsInLine(admin.TabularInline):
    model = OrderFoods
    fields = ['food', 'amount']

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderFoodsInLine]

admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
admin.site.register(Food)
admin.site.register(Order, OrderAdmin)

