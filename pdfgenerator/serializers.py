from rest_framework import serializers
from api.models import Excursions,Checkboxes,Inputs
from .models import FastBooking

class CheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkboxes
        fields = '__all__'

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inputs
        fields = '__all__'

class ExcursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursions
        fields = '__all__'

class FastBookingSerializer(serializers.ModelSerializer):
    inputs = InputSerializer(many=True)
    checkboxes = CheckboxSerializer(many=True)
    #checkboxes.id = serializers.IntegerField(required=False)
    #inputs.id = serializers.IntegerField(required=False)

    class Meta:
        model = FastBooking
        fields = '__all__'
        #id = serializers.IntegerField(required=False)
        #exclude = ()


    def create(self, validated_data):
        inputs_data = validated_data.pop('inputs')
        #inputs_data = (instance.inputs_data).all()

        checkboxes_data = validated_data.pop('checkboxes')
        #checkboxes_data = (instance.inputs_data).all()


        fast_booking = FastBooking.objects.create(**validated_data)
        print(checkboxes_data)

        for input_data in inputs_data:
            input_obj, created = inputs.objects.get_or_create(id=int(input_data['id2']), defaults=input_data)
            fast_booking.inputs.add(input_obj)

        for checkbox_data in checkboxes_data:
            checkbox_obj, created = Checkboxes.objects.get_or_create(id=int(checkbox_data['id2']), defaults=checkbox_data)
            fast_booking.checkboxes.add(checkbox_obj)

        return fast_booking
