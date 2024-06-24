from django.urls import path
from .views import CalculationList, ExcursionsList, BookingCreateView, Id_bookingList

urlpatterns = [
    path('calculation/<int:pk>/', CalculationList.as_view(), name='CalculationList'),  
    path('excursions/', ExcursionsList.as_view(), name='ExcursionsList'),
    path('fast_book/', BookingCreateView.as_view(), name='BookingCreateView'),
]