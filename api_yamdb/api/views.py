from django.shortcuts import render
from rest_framework.views import APIView

from api_yamdb.api.serializers import GetJWSTokenSerializer


class GetJWSToken(APIView):
    def post(self, request):
        serializer = GetJWSTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data


