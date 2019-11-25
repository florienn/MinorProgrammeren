from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('cart', views.cart_view, name='cart'),
    path('user', views.user_view, name='user'),
    path("add", views.add, name="add")
]
