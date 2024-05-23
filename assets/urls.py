from django.urls import path
from .views import *

urlpatterns = [
    path('regions/', RegionListView.as_view(), name='region-list'),
    path('cities/', CityListView.as_view(), name='city-list'),
    path('universities/', UniversityListView.as_view(), name='university-list'),
    path('university/<int:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('studies/', StudyListView.as_view(), name='study-list'),
    path('studies/<int:pk>/', StudyDetailView.as_view(), name='study-detail'),
    path('university-majors/', StudyInUniversityListView.as_view(), name='study-in-university-list'),
    path('university_major/<int:pk>/', StudyInUniversityDetailView.as_view(), name='study-in-university-detail'),
    path('science-pairs/', SciencePairsView.as_view(), name='science-pairs'),
    path('sciences/', ScienceListView.as_view(), name='science-list'),
]