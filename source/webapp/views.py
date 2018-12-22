from webapp.models import Food
from django.views.generic import ListView

class FoodListView(ListView):
    model = Food
    template_name = 'foods.html'
