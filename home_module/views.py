from typing import Any, Dict
from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
        template_name = 'home_module/index_page.html'

        def get_context_data(self, **kwargs):
             context = super().get_context_data(**kwargs)
             context['data'] = 'this is data for home page'
             return context
       

        def site_header_component(request):
             return render(request, 'shared/site_header_component.html')

        def site_footer_component(request):
             return render(request, 'shared/site_footer_component.html')