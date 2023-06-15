from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView
from .models import snacks

# Create your views here.
class home_view_Page(TemplateView):
    template_name = 'home.html'
 
class snack_list_Page(ListView):
    template_name = 'snack_list.html'
    model = snacks
    context_object_name = 'snack_list'

class snack_detail_View(DetailView):
    template_name="snack_detail.html"
    model = snacks
