#employee/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('v1/records/',views.EmployeeListCreateView.as_view()),
    path(
        "v1/records/<int:pk>/",
        views.EmployeeDetailUpdateView.as_view(),
        name="employee-detail-update",
    )
]
