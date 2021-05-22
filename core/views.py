from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from django.shortcuts import render
from .models import UUID
from .utils import get_uuids

class UUIDView(APIView):
    permission_classes = (AllowAny,)

    def get(self,request):
        UUID.objects.create()
        uuids = get_uuids()
        return Response(uuids,status=HTTP_200_OK)
