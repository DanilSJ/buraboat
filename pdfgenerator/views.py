from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FastBooking
from .serializers import FastBookingSerializer

class FastBookingCreateView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = FastBookingSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():

            #serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    print(os.getcwd(),os.listdir())
    return render(request, 'home.html')

def generate_pdf(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        # Генерация HTML для PDF с использованием шаблона Jinja2
        html_string = render_to_string('pdf_template.html', {'name': name, 'phone': phone})
        html = HTML(string=html_string)
        pdf = html.write_pdf()

        # Отправка PDF в ответе
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="contact.pdf"'
        return response
    else:
        return HttpResponse("Method not allowed", status=405)
