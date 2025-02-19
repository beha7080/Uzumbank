from rest_framework import serializers
from .models import Card


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"



class TransacsionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    sender_card = serializers.CharField(max_length=16)
    reciver_card= serializers.CharField(max_length=16)
    money = serializers.FloatField()
