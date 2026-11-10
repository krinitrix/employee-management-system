from django.urls import path
from .views import CustomTokenObtainPairView,UserRegisterView
urlpatterns = [
    path('login/',CustomTokenObtainPairView.as_view(),name='token-obtain'),
    
]
