from django.urls import path
from .views import *

urlpatterns = [
    path('exam/<int:pair_id>/', ExamAPIView.as_view(), name='exam-api'),
]