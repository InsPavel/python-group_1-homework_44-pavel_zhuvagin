from django import forms
from webapp.models import Food, Order, OrderFoods


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []


class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFoods
        exclude = ['order']

class UpdateFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []