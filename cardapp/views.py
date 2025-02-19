from rest_framework import viewsets

from .models import Card
from rest_framework.views import APIView
from .serializers import CarsSerializer, TransacsionSerializer
from rest_framework.response import Response

from usersapp.models import User


class barcha_card(APIView):
    def get(self, request):
        cardlar = Card.objects.all()
        serializer2 = CarsSerializer(cardlar, many=True)
        return Response(serializer2.data)


class Transacsion(APIView):
    serializer_class = TransacsionSerializer

    def post(self, request):
        user_id = request.data.get('user_id')
        sender_card = request.data.get('sender_card')
        reciver_card = request.data.get('sender_card')
        money = float(request.data.get('money'))
        money2 = money - money / 100
        user = Card.objects.all().filter(card_holder=user_id, card_number=sender_card)
        if user:
            for i in user:
                qoldi = i.money - money
                Card.objects.all().filter(card_number=sender_card).update(money=qoldi)
                if i.money >= money:
                    old_money = Card.objects.all().filter(card_number=reciver_card)
                    if old_money:
                        for i in old_money:
                            all_money = Card.objects.all().filter(card_number=reciver_card).update(
                                money=money2 + i.money)

                        return Response({'message': f"Pul jo`natildi {money2}"}, status=201)
                    return Response({'message': f"Bunday karta raqam topilmadi"}, status=404)
                return Response({'message': f"Sizda yetarli Mablag` yoq"}, status=200)
        return Response({"message": 'Bunday foydalanuvchi topilmadi'}, status=404)


class TopMoneyCard(APIView):
    def get(self, request):
        # card = Card.objects.all().order_by('?')
        # card = Card.objects.all().order_by('-money')
        # card = Card.objects.all().order_by('money')
        card = Card.objects.all().order_by('?'), asn(nulls_last=True)
        serializer = CarsSerializer(card, many=True)
        return Response(serializer.data)
