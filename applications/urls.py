from django.urls import path
from .views import (
    ApplyJobView,
    MyApplicationsView,
    UpdateApplicationStatusView
)

urlpatterns = [
    path('apply/', ApplyJobView.as_view(), name='apply-job'),
    path('my/', MyApplicationsView.as_view(), name='my-applications'),
    path('<int:pk>/', UpdateApplicationStatusView.as_view(), name='update-application'),
]