from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import VocaList

urlpatterns = [
    path('', VocaList.as_view(), name = 'voca-list'),
]