from webapp.models import Order, OrderFoods
from django.views.generic import ListView, DetailView

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class OrderDetailList(DetailView):
    model = OrderFoods
    template_name = 'order_detail.html'


