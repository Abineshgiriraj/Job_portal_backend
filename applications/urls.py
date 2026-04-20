from django.urls import path
from .views import ApplyJobView, MyApplicationsView, UpdateApplicationStatusView, RecruiterApplicantsView

urlpatterns = [
    path('apply/', ApplyJobView.as_view(), name='apply-job'),
    path('my-applications/', MyApplicationsView.as_view(), name='my-applications'),
    path('<int:pk>/status/', UpdateApplicationStatusView.as_view(), name='update-application-status'),
    path('recruiter/applicants/', RecruiterApplicantsView.as_view(), name='recruiter-applicants'),
]