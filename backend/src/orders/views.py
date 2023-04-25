from django.views.generic import TemplateView


class OrdersView(TemplateView):
    template_name = "orders/orders.html"
