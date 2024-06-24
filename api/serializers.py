from rest_framework import serializers
from .models import MainHead, MainTextBlock, MainBoats, MainPastTrips, MainTipsToday, MainSequence, New_Module
from dotenv import load_dotenv

load_dotenv()

class MainHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainHead
        fields = ['id', 'slogan', 'mini_slogan', 'background', 'boat', 'excursions']
        depth = 2

class MainTextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTextBlock
        fields = ['id', 'name', 'url', 'description', 'image']
        depth = 2

class MainBoatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBoats
        fields = ['id', 'name', 'size', 'description', 'image', 'slider_number', 'draft_all', 'draft_mobile', 'url_button', 'price']
        depth = 2

class MainPastTripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPastTrips
        fields = ['id', 'name', 'description', 'image', 'slider_number', 'draft_all', 'draft_mobile', 'url_button', 'price']
        depth = 2

class MainPastTripsNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPastTrips
        fields = ['id', 'name', 'description', 'image', 'slider_number', 'draft_all', 'draft_mobile', 'url_button', 'price']
        depth = 2

class MainTipsTodaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTipsToday
        fields = ['id', 'name', 'description', 'image', 'start_time', 'end_time', 'hours', 'slider_number', 'price']
        depth = 2

class MainSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSequence
        fields = ['sequence_json']

    def to_representation(self, instance):
        return instance.sequence_json

class New_ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_Module
        fields = ['id', 'boat', 'text_block', 'past_trips', 'trips_today', 'number']
        depth = 2
