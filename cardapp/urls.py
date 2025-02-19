from django.urls import path
from .views import barcha_card, Transacsion
from django.contrib.auth import get_user_model

User = get_user_model()



urlpatterns = [
    path('all_card/', barcha_card.as_view()),
    path('transacsion/', Transacsion.as_view()),
]
