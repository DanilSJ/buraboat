from django.urls import path
from api.views import MainHeadList, MainTextBlockList, MainBoatsList, MainPastTripsList, MainTipsTodayList, MainSequenceList, New_ModuleList, MainPastTripsNewList, MainPastTripDetail, CreateMainPastTrip

urlpatterns = [
    path('main_head/', MainHeadList.as_view(), name='MainHeadList'),
    path('main_textblock/', MainTextBlockList.as_view(), name='MainTextBlockList'),
    path('main_boats_list/', MainBoatsList.as_view(), name='MainBoatsList'),
    path('main_past_trips/', MainPastTripsList.as_view(), name='MainPastTripsList'),
    path('main_past_trips_new/', MainPastTripsNewList.as_view(), name='MainPastTripsNewList'),
    path('main_tips_today/', MainTipsTodayList.as_view(), name='MainTipsTodayList'),
    path('main_sequence/', MainSequenceList.as_view(), name='MainSequenceList'),
    path('modules/<int:pk>/', New_ModuleList.as_view(), name='New_ModuleList'),
    path('past_trip/<int:pk>/', MainPastTripDetail.as_view(), name='MainPastTripDetail'),
    path('create_past_trip/<int:id>/', CreateMainPastTrip.as_view(), name='CreateMainPastTrip')
]
