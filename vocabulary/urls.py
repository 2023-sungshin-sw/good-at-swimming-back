from django.urls import path

from .views import VocaView

urlpatterns = [
    path('', VocaView.as_view()),
]
