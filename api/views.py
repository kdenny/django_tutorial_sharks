from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse

from .models import Shark, Ping
from .serializers import SharkSerializer

class SharkByIDView(APIView):

    def get(self, request, shark_id='0'):
        if (shark_id != '0'):
            shark = Shark.objects.get(id=shark_id)
            # shark_pings = Ping.objects.filter(shark__id=shark_id).order_by('timestamp')

            serializer = SharkSerializer(shark)
            return Response(serializer.data)

