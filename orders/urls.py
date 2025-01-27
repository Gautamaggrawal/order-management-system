from django.urls import path
from .views import ProductListView, OrderCreateView, OrderDetailView, OrderSuccessView, OrderListView

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('order/', OrderCreateView.as_view(), name="order_create"),
    path('orders/', OrderListView.as_view(), name="order_list"),
    path('order/success/', OrderSuccessView.as_view(), name="order_success"),    
    path('order/<int:id>/', OrderDetailView.as_view(), name="order_details"),
]
