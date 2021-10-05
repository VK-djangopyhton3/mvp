from rest_framework import serializers


class RawDataSerializer(serializers.Serializer):
    """This is the serializer for check data valid or not """
    email = serializers.EmailField(required=True, label="email")
    text = serializers.CharField(required=True, label="text")

