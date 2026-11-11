#employee/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('v1/records/',views.EmployeeListCreateView.as_view()),
    path(
        "v1/records/<int:pk>/",
        views.EmployeeDetailUpdateView.as_view(),
        name="employee-detail-update",
    ),
    path(
        'v1/departments/',
        views.DepartmentListCreateView.as_view(),
        name='department-list-create'
    ),
    path(
        'v1/departments/<int:pk>/',
        views.DepartmentDetailView.as_view(),
        name='department-detail'
    ),
    path('v1/me/',views.MyEmployeeProfileView.as_view(),name='my-employee-profile'),
]
