from django.contrib import admin
from .models import Calc, Inputs, Checkboxes, Settings, Excursions, Booking

class InputsAdmin(admin.ModelAdmin):
    list_display = ('title', 'default_value', 'hint', 'super_hint', 'hour_coefficient', 'trip_coefficient')
  
class CheckboxesAdmin(admin.ModelAdmin):
    list_display = ('title', 'default_value', 'hint', 'super_hint', 'hour_coefficient', 'trip_coefficient')

class CalcAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'date')

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'start_time', 'end_time')

class ExcursionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'description', 'image_for_tab', 'number', 'prive_hour', 'prive', 'prive_hourr', 'privee')
    search_fields = ['name']


admin.site.register(Inputs, InputsAdmin)
admin.site.register(Checkboxes, CheckboxesAdmin)
admin.site.register(Calc, CalcAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Excursions, ExcursionsAdmin)
admin.site.register(Booking)