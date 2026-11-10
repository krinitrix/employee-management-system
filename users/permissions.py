from rest_framework.permissions import BasePermission


class IsHRAdmin(BasePermission):
  """Allows access only to authenticated users with the HR_ADMIN role."""

  def has_permission(self, request, view):
    
    return (
         getattr(request.user, "role", None) == "HR_ADMIN"
    )