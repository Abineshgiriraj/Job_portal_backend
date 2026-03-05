from django.urls import path
from .views import JobListView, JobCreateView, JobDetailView, MyJobListView


urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('create/', JobCreateView.as_view(), name='job-create'),
    path('my-jobs/', MyJobListView.as_view(), name='my-job-list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
]