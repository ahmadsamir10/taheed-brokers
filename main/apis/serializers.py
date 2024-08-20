from rest_framework import serializers
from main.models import BrokerRequest

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrokerRequest
        fields = ['name', 'mobile_number', 'expected_transaction_amounts_per_month', 'region', 'years_of_experience']
