from django.contrib import admin
from .models import MainHead, MainTextBlock, MainBoats, MainPastTrips, MainTipsToday, MainSequence, New_Module

class MainHeadAdmin(admin.ModelAdmin):
    list_display = ('slogan', 'mini_slogan', 'background', 'boat')
class MainTextBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'image')
    search_fields = ['name']

class MainBoatsAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'description', 'image', 'slider_number', 'draft_all', 'draft_mobile', 'url_button')
    search_fields = ['name']

class MainPastTripsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'slider_number', 'draft_all', 'draft_mobile', 'url_button')
    search_fields = ['name']

class MainTipsTodayAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'image', 'start_time', 'end_time', 'hours', 'slider_number', 'price')
    search_fields = ['name']

class MainSequenceAdmin(admin.ModelAdmin):
    list_display = ('sequence_json',)
    
class New_ModuleAdmin(admin.ModelAdmin):
    list_display = ('number',)

admin.site.register(MainHead, MainHeadAdmin)
admin.site.register(MainTextBlock, MainTextBlockAdmin)
admin.site.register(MainBoats, MainBoatsAdmin)
admin.site.register(MainPastTrips, MainPastTripsAdmin)
admin.site.register(MainTipsToday, MainTipsTodayAdmin)
admin.site.register(MainSequence, MainSequenceAdmin)
admin.site.register(New_Module, New_ModuleAdmin)
