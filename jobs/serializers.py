from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'description',
            'salary',
            'location',
            'experience_level',
            'company',
            'company_name',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']