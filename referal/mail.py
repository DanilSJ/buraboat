from requests import Response
from django.core.mail import send_mail
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(
        recipient: str, subject: str, content: str,
        content_type: str = "text/plain"
) -> Response:
    response = send_mail(
        subject=subject,
        message=content,
        from_email=os.getenv('FROM_EMAIL', 'Default-Value') ,
        recipient_list=[recipient]
    )
    return response

