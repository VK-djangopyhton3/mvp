from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from mvp.apps.core.serializers import RawDataSerializer
from mvp.common.permissions import UserCheckEmailOrTranslatorPermissions
from mvp.common.utils import return_response


class EmailCheckAndTranslatorAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RawDataSerializer

    def post(self, request, *args, **kwargs):
        """Post basic data and get the response"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            """Check user have permission and return response accordingly """
            is_user = UserCheckEmailOrTranslatorPermissions.has_permission(request, data)

            return return_response(data, True, 'Successful!', status.HTTP_200_OK)

        return return_response(serializer.errors, False, 'Failed!', status.HTTP_400_BAD_REQUEST)