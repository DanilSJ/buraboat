from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from referal.views import referal, referal_ref, register, success_code, login, ForgotPassword, ForgotPasswordSuccess
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from calculation.views import Id_bookingList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('success_code/', success_code, name='success_code'),
    path('login/', login, name='login'),
    path('referal/', referal, name='referal'),
    path('referal/ref_param/<int:pk>/', referal_ref, name='referal_ref'),
    path('ForgotPassword/', ForgotPassword, name='ForgotPassword'),
    path('ForgotPasswordSuccess/<int:pk>/', ForgotPasswordSuccess, name='ForgotPasswordSuccess'),
    
    path('id_booking/<int:pk>/', Id_bookingList, name='Id_bookingList'),  
    
    # API 
    
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),

    path('swagger-ui/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),

    path('api/v1/', include('api.urls')),
    path('api/v1/', include('calculation.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
