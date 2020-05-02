from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    order = serializers.ListField(child=serializers.FloatField())

    def validate_order(self, order):
        for x in order:
            if x<0:
                raise serializers.ValidationError("Error: Quantity can't be neagative.")
            elif (not(x%1==0)):
                raise serializers.ValidationError("Error: Quantity can't be a fraction.")
        return order