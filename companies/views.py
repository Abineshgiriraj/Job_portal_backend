from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Company
from .serializers import CompanySerializer
from .permissions import IsRecruiter
from rest_framework import generics, permissions

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]

class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsRecruiter]

    def perform_create(self, serializer):
        if self.request.user.company:
            raise ValidationError("Recruiter already owns a company.")

        company = serializer.save()
        self.request.user.company = company
        self.request.user.save()