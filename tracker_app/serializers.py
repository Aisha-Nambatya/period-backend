from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, PeriodLog, SymptomLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    next_period_start_date = serializers.SerializerMethodField()
    ovulation_start_date = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_next_period_start_date(self, obj):
        return obj.next_period_start_date()

    def get_ovulation_start_date(self, obj):
        return obj.ovulation_start_date()

class PeriodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodLog
        fields = '__all__'

class SymptomLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomLog
        fields = '__all__'
