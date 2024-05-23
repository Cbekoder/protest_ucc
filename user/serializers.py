from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import *

class PhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Bu raqam bilan boshqa foydalanuvchi ro'yxatdan o'tgan")
        return value

class SMSVerificationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)
    code = serializers.CharField(max_length=4)

class SetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

class CompleteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'birthday', 'city', 'gender', 'image']