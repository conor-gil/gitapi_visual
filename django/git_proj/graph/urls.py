# graph/urls.py
from django.urls import path

from .views import HomePageView, PiePageView, HistoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pie/', PiePageView.as_view(), name='pie'),
    path('histo/', HistoPageView.as_view(), name='histo')
]