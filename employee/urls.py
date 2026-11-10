#employee/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('v1/records/',views.EmployeeCreateView.as_view()),
]
