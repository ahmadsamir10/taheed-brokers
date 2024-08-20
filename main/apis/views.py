from rest_framework import generics
from django.core.mail import send_mail
from main.models import BrokerRequest
from main.apis.serializers import BrokerSerializer
from main.utils.emails import send_registration_email


class BrokerRegistrationView(generics.CreateAPIView):
    queryset = BrokerRequest.objects.all()
    serializer_class = BrokerSerializer

    def perform_create(self, serializer):
        broker = serializer.save()
        # Send email to the client after registration
        send_registration_email(broker)
