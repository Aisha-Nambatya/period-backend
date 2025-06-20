from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', views.UserProfileDetail.as_view(), name='profile'),
    path('periods/', views.PeriodLogListCreate.as_view(), name='periods'),
    path('symptoms/', views.SymptomLogListCreate.as_view(), name='symptoms'),
]
