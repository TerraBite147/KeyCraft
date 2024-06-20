from django.core.mail import send_mail
from django.conf import settings


def send_subscription_email(email):
    subject = 'Thank You for Subscribing!'
    message = 'Thank you for subscribing to our newsletter. We will keep you updated with the latest news.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
