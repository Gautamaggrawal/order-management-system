from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Order
from .forms import OrderForm

class ProductListView(ListView):
    model = Product
    template_name = "orders/product_list.html"
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(available=True)

class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = 'orders'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('product')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/create_order.html"
    success_url = reverse_lazy('order_success')


class OrderDetailView(DetailView):
    slug_field = "id"
    slug_url_kwarg = "id"
    model = Order
    template_name = "orders/order_detail.html"


class OrderSuccessView(TemplateView):
    template_name = "orders/order_success.html"
