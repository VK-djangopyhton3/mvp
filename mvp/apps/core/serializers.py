from rest_framework import serializers


class RawDataSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, label="email")
    text = serializers.CharField(required=True, label="text")

