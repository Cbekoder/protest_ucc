from django.contrib import admin
from .models import Region, City, University, Study, StudyInUniversity

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

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('study_name', 'study_code', 'science_1', 'science_2')
    search_fields = ('study_name', 'study_code')

@admin.register(StudyInUniversity)
class StudyInUniversityAdmin(admin.ModelAdmin):
    list_display = ('university', 'study', 'grant_ball', 'contract_ball', 'grant_count', 'contract_count')
    list_filter = ('university', 'study')
