from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Connect
from .serializers import PriceSerializer


# Create your views here.
class ConnectViewSet(APIView):
    def get(self, request):

        queryset = Connect.objects.all()
        serializer = PriceSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



# router = routers.DefaultRouter()
# router.register(r'price', ConnectViewSet)

