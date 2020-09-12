from rest_framework.serializers import ModelSerializer
from ..models import *


# to retrive specific field/s from DB into query set
class CoffeeMachineSerializer(ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = ['SKU']


class CoffeePodSerializer(ModelSerializer):
    class Meta:
        model = CoffeePod
        fields = ['SKU']
