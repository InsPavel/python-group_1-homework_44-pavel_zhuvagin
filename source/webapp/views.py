from django.views.generic import DetailView, CreateView, ListView, UpdateView, View, DeleteView, FormView
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from webapp.models import Food, Order, OrderFoods, User
from webapp.forms import FoodForm, OrderForm, OrderFoodForm, UpdateFoodForm, UpdateOrderForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

class OrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'
    permission_required = 'webapp.view_order'

class OrderDetailList(LoginRequiredMixin, DetailView, FormView):
    model = Order
    template_name = 'order_detail.html'
    form_class = OrderFoodForm

# Добавление блюд в заказ через Ajax запрос

class OrderFoodAjaxCreateView(CreateView):
    model = OrderFoods
    form_class = OrderFoodForm

    def form_valid(self, form):
        order = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        form.instance.order = order
        order_food = form.save()
        return JsonResponse({
            'food_name': order_food.food.name,
            'food_pk': order_food.food.pk,
            'amount': order_food.amount,
            'pk': order_food.pk,
            'edit_url': reverse('webapp:order_food_update', kwargs={'pk': order_food.pk}),
            'delete_url': reverse('webapp:order_food_delete', kwargs={'pk': order_food.pk})
        })


    def form_invalid(self, form):
        return JsonResponse({
            'errors': form.errors
        }, status='422')

# Изменение блюд в заказе через Ajax запрос

class OrderFoodAjaxUpdateView(UpdateView):
    model = OrderFoods
    form_class = OrderFoodForm

    def form_valid(self, form):
        order_food = form.save()
        return JsonResponse({
            'food_name': order_food.food.name,
            'food_pk': order_food.food.pk,
            'amount': order_food.amount,
            'pk': order_food.pk,
        })


    def form_invalid(self, form):
        return JsonResponse({
            'errors': form.errors
        }, status='422')

# Удаление блюд из заказа через Alax запрос

class OrderFoodAjaxDeleteView(DeleteView):
    def get(self, request, *args, **kwargs):
        orderfoods = OrderFoods.objects.get(pk=kwargs['pk'])
        orderfoods.delete()

        return JsonResponse({
            'pk': kwargs['pk'],
        })

class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm
    permission_required = 'webapp.edit_order_food'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.operator = self.request.user
        return super().form_valid(form)

class OrderFoodCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = OrderFoods
    form_class = OrderFoodForm
    template_name = 'order_food_create.html'
    permission_required = 'webapp.edit_order_food'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food
    template_name = 'food_detail.html'

class FoodCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_create.html'
    permission_required = 'webapp.edit_order_food'

    def get_success_url(self):
        return reverse('webapp:food_detail', kwargs={'pk': self.object.pk})

class FoodListView(LoginRequiredMixin, ListView):
    model = Food
    template_name = 'food_list.html'

class FoodUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Food
    form_class = UpdateFoodForm
    template_name = 'food_update.html'
    permission_required = 'webapp.edit_order_food'

    def get_success_url(self):
        return reverse('webapp:food_detail', kwargs={'pk': self.object.pk})

class OrderFoodsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('webapp:food_list')
    permission_required = 'webapp.edit_order_food'


class OrderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Order
    form_class = UpdateOrderForm
    template_name = 'order_update.html'
    permission_required = 'webapp.edit_order_food'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})

class OrderDeliverView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'webapp.сan_take_order_or_deliver'
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order.status == 'preparing':
            order.status = "on_way"
            order.courier = request.user
        elif order.status == 'on_way':
            if order.courier == request.user:
                order.status = 'delivered'
                order.courier = request.user
        order.save()

        return redirect('webapp:order_detail', order.pk)

class OrderCancelView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'webapp.edit_order_food'
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.status = 'canceled'
        order.save()
        return redirect('webapp:order_detail', order.pk)










