from django.urls import path
from . import views

urlpatterns = [
    path(
        'v1/records/',
        views.PayrollListCreateView.as_view(),
        name='payroll-list-create'
    ),
    path('v1/me/',views.MyPayrollListView.as_view(),name='my-payroll-list'),
]