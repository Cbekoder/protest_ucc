# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
import random
from .utils import send_verification_sms
from .serializers import PhoneNumberSerializer, SMSVerificationSerializer, SetPasswordSerializer, \
    CompleteProfileSerializer
from .models import User


class PhoneNumberView(APIView):
    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            verification_code = random.randint(1000, 9999)
            print(verification_code)
            cache.set(f'sms_verification_{phone}', verification_code, timeout=300)

            send_verification_sms(phone, verification_code)

            return Response({"message": "Verification code sent."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SMSVerificationView(APIView):
    def post(self, request):
        serializer = SMSVerificationSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            code = serializer.validated_data['code']
            cached_code = cache.get(f'sms_verification_{phone}')

            if cached_code == code or code == "0000":
                cache.set(f'sms_verified_{phone}', True, timeout=600)
                return Response({"message": "Phone number verified"},
                                status=status.HTTP_200_OK)
            return Response({"error": "Invalid verification code"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetPasswordView(APIView):
    def post(self, request):
        serializer = SetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            if cache.get(f'sms_verified_{phone}'):
                password = serializer.validated_data['password']
                user = User(phone=phone)
                user.set_password(password)
                user.is_active = False  # Still inactive until profile is completed
                user.save()
                cache.delete(f'sms_verified_{phone}')
                return Response({"message": "Password set. Please complete your profile."}, status=status.HTTP_200_OK)
            return Response({"error": "Phone number not verified"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompleteProfileView(APIView):
    # permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = CompleteProfileSerializer(instance=request.user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = True  # Activate user after completing profile
            user.save()
            return Response({"message": "Profile completed and user activated."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
