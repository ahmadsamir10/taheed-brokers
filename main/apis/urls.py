from django.urls import path
from main.apis.views import BrokerRegistrationView

urlpatterns = [
    path('register/', BrokerRegistrationView.as_view(), name='broker-registration-api'),
]