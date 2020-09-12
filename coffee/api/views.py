from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from ..models import *


class CoffeeMachines(APIView):
    # check authentication and permissions but in our case there are not both of them
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def post(request):
        # get data from request
        product_type = request.data.get('product_type', None)
        coffee_machine_models = request.data.get('coffee_machine_models', None)
        water_line_compatible = request.data.get('water_line_compatible', None)

        # get data from DB depending on data from request
        if not water_line_compatible and not coffee_machine_models:
            json_data = CoffeeMachineSerializer(
                CoffeeMachine.objects.filter(product_type=product_type, ), many=True).data
        elif not product_type and not coffee_machine_models:
            json_data = CoffeeMachineSerializer(
                CoffeeMachine.objects.filter(water_line_compatible=water_line_compatible), many=True).data
        elif not water_line_compatible:
            json_data = CoffeeMachineSerializer(
                CoffeeMachine.objects.filter(product_type=product_type,
                                             coffee_machine_models=coffee_machine_models, ),
                many=True).data
        elif not coffee_machine_models:
            json_data = CoffeeMachineSerializer(
                CoffeeMachine.objects.filter(product_type=product_type,
                                             water_line_compatible=water_line_compatible, ),
                many=True).data
        else:
            json_data = CoffeeMachineSerializer(
                CoffeeMachine.objects.filter(product_type=product_type,
                                             water_line_compatible=water_line_compatible,
                                             coffee_machine_models=coffee_machine_models, ),
                many=True).data

        # check if there is data or not and set response status
        global_status = status.HTTP_200_OK

        if len(json_data) == 0:
            json_data = {"error": "Please enter a valid data"}
            global_status = status.HTTP_400_BAD_REQUEST

        return Response(json_data, global_status)


class CoffeePods(APIView):
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def post(request):
        product_type = request.data.get('product_type', None)
        coffee_flavor = request.data.get('coffee_flavor', None)
        pack_size = request.data.get('pack_size', None)

        if not pack_size and not coffee_flavor:
            json_data = CoffeePodSerializer(
                CoffeePod.objects.filter(product_type=product_type), many=True).data
        elif not product_type and not pack_size:
            json_data = CoffeePodSerializer(
                CoffeePod.objects.filter(coffee_flavor=coffee_flavor), many=True).data
        elif not product_type and not coffee_flavor:
            json_data = CoffeePodSerializer(
                CoffeePod.objects.filter(pack_size=pack_size), many=True).data
        elif not pack_size:
            json_data = CoffeePodSerializer(
                CoffeePod.objects.filter(product_type=product_type,
                                         coffee_flavor=coffee_flavor, ),
                many=True).data
        elif not coffee_flavor:
            json_data = CoffeePodSerializer(
                CoffeePod.objects.filter(product_type=product_type,
                                         pack_size=pack_size, ),
                many=True).data
        else:
            json_data = CoffeePodSerializer(
                CoffeePod.objects.filter(product_type=product_type,
                                         pack_size=pack_size,
                                         coffee_flavor=coffee_flavor, ),
                many=True).data

        global_status = status.HTTP_200_OK

        if len(json_data) == 0:
            json_data = {"error": "Please enter a valid data"}
            global_status = status.HTTP_400_BAD_REQUEST

        return Response(json_data, global_status)
