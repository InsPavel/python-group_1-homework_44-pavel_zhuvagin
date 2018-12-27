from django.urls import path
from webapp import views
from webapp.views import OrderListView, OrderDetailList, OrderCreateView, FoodCreateView, \
    FoodDetailView, OrderFoodCreateView, FoodListView, FoodUpdateView, \
    OrderFoodsDeleteView, OrderUpdateView, OrderDeliverView, OrderCancelView

app_name = 'webapp'

urlpatterns = [
    path('', OrderListView.as_view(), name='order'),
    path('order/<int:pk>', OrderDetailList.as_view(), name='order_detail'),
    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('food/create', FoodCreateView.as_view(), name='food_create'),
    path('food/<int:pk>', FoodDetailView.as_view(), name='food_detail'),
    path('order/<int:pk>/food/create', OrderFoodCreateView.as_view(), name='order_food_create'),
    path('food', FoodListView.as_view(), name='food_list'),
    path('food/<int:pk>/update', FoodUpdateView.as_view(), name='food_update'),
    path('order/<int:pk>/food/delete', OrderFoodsDeleteView.as_view(), name='food_delete'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/deliver', OrderDeliverView.as_view(), name='order_deliver'),
    path('order/<int:pk>/cancel', OrderCancelView.as_view(), name='order_cancel'),
]