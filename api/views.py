# views.py
from rest_framework import generics
from .models import MainHead, MainTextBlock, MainBoats, MainPastTrips, MainTipsToday, MainSequence, New_Module
from .serializers import MainHeadSerializer, MainTextBlockSerializer, MainBoatsSerializer, MainPastTripsSerializer, MainTipsTodaySerializer, MainSequenceSerializer, New_ModuleSerializer, MainPastTripsNewSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class MainHeadList(generics.ListAPIView):
    queryset = MainHead.objects.all()
    serializer_class = MainHeadSerializer

class MainTextBlockList(generics.ListAPIView):
    queryset = MainTextBlock.objects.all()
    serializer_class = MainTextBlockSerializer

class MainBoatsList(generics.ListAPIView):
    queryset = MainBoats.objects.all().order_by('slider_number')
    serializer_class = MainBoatsSerializer

class MainPastTripsList(generics.ListAPIView):
    queryset = MainPastTrips.objects.filter(page=True).order_by('slider_number')
    serializer_class = MainPastTripsSerializer
    
class MainPastTripsPagination(PageNumberPagination):
    page_size = 10  # Устанавливаем количество элементов на странице
    page_size_query_param = 'page_size'
    max_page_size = 100

class MainPastTripsNewList(generics.ListAPIView):
    queryset = MainPastTrips.objects.all().order_by('slider_number')
    serializer_class = MainPastTripsNewSerializer
    pagination_class = MainPastTripsPagination  # Добавляем пагинацию
    
class MainPastTripDetail(generics.RetrieveAPIView):
    queryset = MainPastTrips.objects.all()
    serializer_class = MainPastTripsNewSerializer 

class CreateMainPastTrip(APIView):
    def post(self, request, id, *args, **kwargs):
        serializer = MainPastTripsNewSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(id=id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    

class MainTipsTodayList(generics.ListAPIView):
    queryset = MainTipsToday.objects.all().order_by('slider_number')
    serializer_class = MainTipsTodaySerializer

class MainSequenceList(generics.ListAPIView):
    serializer_class = MainSequenceSerializer
    
    def get_queryset(self):
        queryset = MainSequence.objects.all()
        first_element = queryset.first()
        return queryset.filter(pk=first_element.pk) if first_element else queryset.none()
    
class New_ModuleList(generics.RetrieveAPIView):
    queryset = New_Module.objects.all()
    serializer_class = New_ModuleSerializer
    lookup_field = 'pk'
