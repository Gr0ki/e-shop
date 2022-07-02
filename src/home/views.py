from django.views.generic import TemplateView
from datetime import datetime


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
