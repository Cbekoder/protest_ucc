from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/phone/', PhoneNumberView.as_view(), name='register_phone'),
    path('register/verify-sms/', SMSVerificationView.as_view(), name='verify_sms'),
    path('register/set-password/', SetPasswordView.as_view(), name='set_password'),
    path('register/complete-profile/', CompleteProfileView.as_view(), name='complete_profile'),
]