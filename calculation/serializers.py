from rest_framework import serializers
from .models import Excursions, Calc, Booking
from .mail import send_mail
from dotenv import load_dotenv
import os
import qrcode
from fpdf import FPDF
import os
from PIL import Image

from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

load_dotenv()

def transliterate(text):
    translit_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E',
        'Ю': 'Yu', 'Я': 'Ya', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': ' '
    }

    transliterated_text = ''.join([translit_dict.get(char, char) for char in text])

    return transliterated_text


class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calc
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Check if context has request object
        request = kwargs['context'].get('request') if 'context' in kwargs else None

        # If request method is GET and depth=2 is requested, modify fields attribute
        if request and request.method == 'GET' and request.query_params.get('depth') == '3':
            kwargs['depth'] = 3  # Set depth=2 for nested serialization

        super().__init__(*args, **kwargs)

class ExcursionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursions
        fields = '__all__'
        depth = 2


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'excursion_id', 'start_time', 'end_time', 'day', 'inputs', 'checkboxes', 'description', 'front', 'referal']

    def create(self, validated_data):
        request = self.context.get('request')
        booking = Booking.objects.create(**validated_data)

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"{os.getenv('MAIN_HOST_PATH', 'Default-Value')}/id_booking/{booking.id}/")
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image = qr_image.resize((180, 180))  # Resize QR code to 180x180 pixels

        qr_path = f"media/qr/qr_id_booking_{booking.id}.png"
        qr_image.save(qr_path)

        # Create PDF
        output_pdf_path = f"media/pdf/ticket_{booking.id}.pdf"

        # Define styles for the PDF
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        subtitle_style = styles['Heading2']
        normal_style = styles['Normal']

        doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
        story = []

        # Title
        title = Paragraph("Booking Confirmation", title_style)
        story.append(title)
        story.append(Spacer(1, 12))

        # Booking details
        booking_details = [
            f"<b>Booking Number:</b> {booking.id}",
            f"<b>Price:</b> 0",  # Replace with actual price if available
            f"<b>Text:</b> good",  # Replace with actual text if available
            f"<b>DAY:</b> {booking.day}",
            f"<b>Start Time:</b> {booking.start_time}",
            f"<b>End Time:</b> {booking.end_time}",
            f"<b>Description:</b> {booking.description}",
            f"<b>QR Code Text:</b> {os.getenv('MAIN_HOST_PATH', 'Default-Value')}/id_booking/{booking.id}/",
        ]

        for detail in booking_details:
            detail_para = Paragraph(detail, normal_style)
            story.append(detail_para)
            story.append(Spacer(1, 6))

        # Add QR code
        qr_image_path = qr_path  # Path to resized QR code
        qr_image = Image(qr_image_path, width=180, height=180)
        story.append(qr_image)

        # Build the PDF
        doc.build(story)

        # Send email with booking details
        try:
            send_mail(
                subject='Booking Confirmation',
                message=f"Booking details:\n\n{text}",
                from_email=os.getenv('EMAIL_OWNER_HO', 'Default-Value'),
                recipient_list=[validated_data['email']],
                fail_silently=False,
            )
        except Exception:
            pass

        return booking
        
    def to_representation(self, instance):
        qr_code_path = f"media/qr/qr_id_booking_{instance.id}.png"

        # Ensure QR code is resized to 180x180 pixels
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"{os.getenv('MAIN_HOST_PATH', 'Default-Value')}/id_booking/{instance.id}/")
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image = qr_image.resize((180, 180))  # Resize QR code to 180x180 pixels

        qr_image.save(qr_code_path)

        # Return representation
        return {
            'id_booking': instance.id,
            'price': 'starts from 200 eu',
            'text': 'Your booking was successful!',
            'qr_code_url': f"{os.getenv('MAIN_HOST_PATH', 'Default-Value')}/{qr_code_path}",
            'qr_code_text': 'Your booking was successful! +382 69 665 667 whatsApp, Viber, phone If you have any questions or need further information, please feel free to contact us',
            'link_download_ticket': f"{os.getenv('MAIN_HOST_PATH', 'Default-Value')}/media/pdf/ticket_{instance.id}.pdf/"
        }
