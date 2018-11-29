# pages/graph.py
from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'home.html'

class PiePageView(TemplateView):
    template_name = 'pie.html'

class HistoPageView(TemplateView):
    template_name = 'histo.html'