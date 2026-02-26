from django.urls import path
from .views import CompanyCreateView, CompanyListView


urlpatterns = [
    path('', CompanyListView.as_view(), name='company-list'),
    path('create/', CompanyCreateView.as_view(), name='company-create'),
]