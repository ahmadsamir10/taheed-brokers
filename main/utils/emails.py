import threading
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings



def send_registration_email(broker):
    # Company email
    company_email = settings.TAHEED_EMAIL # "info@taheed.com"
    
    # Broker information
    name = broker.name
    mobile_number = broker.mobile_number
    transaction_amounts = broker.expected_transaction_amounts_per_month
    region = broker.region
    years_of_experience = broker.years_of_experience
    
    # Date in Arabic format
    date_arabic = timezone.now().strftime('%d-%m-%Y')
    
    # Prepare email content in Arabic
    subject = "تسجيل وسيط جديد"
    
    # Email body in Arabic
    body = f"""
    تم تسجيل وسيط جديد في النظام:
    
    الاسم: {name}
    رقم الجوال: {mobile_number}
    مبالغ الصفقات المتوقعة شهريًا: {transaction_amounts}
    المنطقة: {region}
    سنوات الخبرة: {years_of_experience}
    تاريخ التسجيل: {date_arabic}
    """
    
    # Send the email
    def send_email():
        send_mail(
            subject,
            body,
            settings.NO_REPLY_TAHEED_EMAIL,  # Replace with your no-reply or system email
            [company_email],
            fail_silently=False,
        )

    email_thread = threading.Thread(target=send_email)
    email_thread.start()    