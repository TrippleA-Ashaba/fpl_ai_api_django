from django.shortcuts import render
from django.views.generic import TemplateView

from .get_data import get_game_data

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"
    extra_context = {"game_data": get_game_data}
