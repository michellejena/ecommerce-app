from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('products/', views.product_list, name='products'),
    path('add/<int:product_id>/', views.add_to_cart, name='add'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('thank-you/', views.thank_you, name='thank_you'),
]