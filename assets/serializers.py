from rest_framework import serializers
from .models import *
from exam.serializers import Science1Serializer

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'region']

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'

class StudyInUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyInUniversity
        fields = '__all__'

class SciencePairsSerializer(serializers.ModelSerializer):
    science_2 = Science1Serializer()

    class Meta:
        model = SciencePairs
        fields = ['id', 'science_2']

class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = ("name",)

