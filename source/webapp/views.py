from django.views.generic import DetailView, CreateView, ListView, UpdateView, View, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from webapp.models import Food, Order, OrderFoods
from webapp.forms import FoodForm, OrderForm, OrderFoodForm, UpdateFoodForm, UpdateOrderForm


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class OrderDetailList(DetailView):
    model = OrderFoods
    template_name = 'order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

class OrderFoodCreateView(CreateView):
    model = OrderFoods
    form_class = OrderFoodForm
    template_name = 'order_food_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'

class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_create.html'

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})

class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'

class FoodUpdateView(UpdateView):
    model = Food
    form_class = UpdateFoodForm
    template_name = 'food_update.html'

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})

class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('food_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = UpdateOrderForm
    template_name = 'order_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

