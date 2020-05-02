from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    order = serializers.ListField(child=serializers.FloatField())
