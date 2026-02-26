from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsJobSeeker, IsRecruiterOwner


class ApplyJobView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsJobSeeker]

    def perform_create(self, serializer):
        job = serializer.validated_data['job']
        user = self.request.user

        if Application.objects.filter(job=job, applicant=user).exists():
            raise ValidationError("You already applied to this job.")

        serializer.save(applicant=user)


class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsJobSeeker]

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)


class UpdateApplicationStatusView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsRecruiterOwner]
    http_method_names = ['patch']