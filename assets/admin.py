from django.contrib import admin
from .models import *

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'abbr_name', 'phone', 'address')
    search_fields = ('full_name', 'abbr_name', 'phone', 'address')

@admin.register(SciencePairs)
class SciencePairsAdmin(admin.ModelAdmin):
    list_display = ('science_1', 'science_2')
    search_fields = ('science_1__name', 'science_2__name')

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('study_name', 'study_code', 'sciencePair')
    search_fields = ('study_name', 'study_code')

@admin.register(StudyInUniversity)
class StudyInUniversityAdmin(admin.ModelAdmin):
    list_display = ('university', 'study', 'grant_ball', 'contract_ball', 'grant_count', 'contract_count')
    list_filter = ('university', 'study')

@admin.register(ImportantSciencePairs)
class ImportantSciencePairsAdmin(admin.ModelAdmin):
    list_display = ('science_1', 'science_2', 'science_3')
    search_fields = ('science_1__name', 'science_2__name', 'science_3__name')

@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
