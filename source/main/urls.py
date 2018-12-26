"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import OrderListView, OrderDetailList, OrderCreateView, FoodCreateView, \
    FoodDetailView, OrderFoodCreateView, FoodListView, FoodUpdateView, \
    OrderFoodsDeleteView, OrderUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
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
    path('edit/<int:pk>/', views.edit, name='order_deliver'),
    path('cancel/<int:pk>/', views.cancel, name='order_cancel'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
