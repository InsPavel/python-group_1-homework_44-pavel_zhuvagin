from django.urls import path
from webauth.views import login_view, logout_view

app_name = 'webauth'

urlpatterns = [
    path('auth/login', login_view, name='login'),
    path('auth/logout', logout_view, name='logout')
]