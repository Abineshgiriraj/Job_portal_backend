from rest_framework.permissions import BasePermission


class IsJobSeeker(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'job_seeker'
        )


class IsRecruiterOwner(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'recruiter'
        )

    def has_object_permission(self, request, view, obj):
        return obj.job.company == request.user.company