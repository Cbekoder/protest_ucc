from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import *
from .serializers import *


class RegionListView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CityListView(APIView):
    def get(self, request):
        region_id = request.query_params.get('r')
        if not region_id:
            cities = City.objects.all()
            serializer = CitySerializer(cities, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            region = Region.objects.get(id=region_id)
        except Region.DoesNotExist:
            return Response({'error': 'Region not found'}, status=status.HTTP_404_NOT_FOUND)

        cities = City.objects.filter(region=region)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UniversityListView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDetailView(generics.RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

# class StudyListView(generics.ListAPIView):
#     queryset = Study.objects.all()
#     serializer_class = StudySerializer

class StudyDetailView(generics.RetrieveAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

class StudyInUniversityListView(generics.ListAPIView):
    queryset = StudyInUniversity.objects.all()
    serializer_class = StudyInUniversitySerializer

class StudyInUniversityDetailView(generics.RetrieveAPIView):
    queryset = StudyInUniversity.objects.all()
    serializer_class = StudyInUniversitySerializer

class SciencePairsView(APIView):
    def get(self, request):
        sciences = Science.objects.all()
        response_data = []

        for science in sciences:
            science_pairs = SciencePairs.objects.filter(science_1=science)
            pairs_serializer = SciencePairsSerializer(science_pairs, many=True)
            response_data.append({
                "science": science.name,
                "pairs": pairs_serializer.data
            })

        return Response(response_data, status=status.HTTP_200_OK)

class ScienceListView(APIView):
    def get(self, request):
        sciences = Science.objects.all()
        serializer = ScienceSerializer(sciences, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudyListView(APIView):
    def get(self, request):
        studies = Study.objects.all()
        data = []
        for study in studies:
            sciences_data = {}
            if study.sciencePair:
                science_pairs = study.sciencePair
                science_1 = science_pairs.science_1
                science_2 = science_pairs.science_2
                sciences_data["science1"] = ScienceSerializer(science_1).data.get("name")
                sciences_data["science2"] = ScienceSerializer(science_2).data.get("name")
            data.append({
                "study_name": study.study_name,
                "study_code": study.study_code,
                "science_pairs": study.sciencePair.id,
                "sciences": sciences_data
            })
        return Response(data)