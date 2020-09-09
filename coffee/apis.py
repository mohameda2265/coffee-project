from rest_framework.views import APIView
from rest_framework.response import Response

class coffee_machines(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = request
        print("machines")
        print(data)
        return Response()


class coffee_pods(APIView):
    authentication_classes = []
    permission_classes = []
    print("pods")
