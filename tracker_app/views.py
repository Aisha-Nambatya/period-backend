from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import UserProfile, PeriodLog, SymptomLog
from .serializers import (
    UserSerializer, UserProfileSerializer, PeriodLogSerializer, SymptomLogSerializer
)

# Register User
class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = UserProfile.objects.create(user=user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id})

# Get Profile
class UserProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

# Period Logs
class PeriodLogListCreate(generics.ListCreateAPIView):
    serializer_class = PeriodLogSerializer

    def get_queryset(self):
        return PeriodLog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Symptom Logs
class SymptomLogListCreate(generics.ListCreateAPIView):
    serializer_class = SymptomLogSerializer

    def get_queryset(self):
        return SymptomLog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
