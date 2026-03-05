from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Job
from .serializers import JobSerializer
from .filters import JobFilter
from .permissions import IsRecruiter


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = JobFilter

    search_fields = ['title']
    ordering_fields = ['salary', 'created_at']


class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]


class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)


class MyJobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]

    def get_queryset(self):
        return Job.objects.filter(recruiter=self.request.user).order_by('-created_at')
        