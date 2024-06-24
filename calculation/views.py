from .serializers import ExcursionsSerializer, CalculationSerializer
from .models import Excursions, Calc, Booking
from rest_framework import generics
from .serializers import BookingSerializer
from django.shortcuts import render

class ExcursionsList(generics.ListAPIView):
    queryset = Excursions.objects.all()
    serializer_class = ExcursionsSerializer


class CalculationList(generics.RetrieveAPIView):
    serializer_class = CalculationSerializer

    def get_queryset(self):
        excursion_pk = self.kwargs.get('pk')
        return Calc.objects.filter(excursions__pk=excursion_pk)

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response


def Id_bookingList(request, pk):
    data = Booking.objects.get(id=pk)


    context = {
        'data': data
    }

    return render(request, 'booking/index.html', context=context)
