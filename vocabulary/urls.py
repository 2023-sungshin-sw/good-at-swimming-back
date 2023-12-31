from django.urls import path

from .views import *

urlpatterns = [
    path('', VocaList.as_view(), name='voca-list'),
    path('exam', VocaTestList.as_view(), name='voca-test-list'),
    path('exam/meaning', MeaningView.as_view(), name='voca-test-meaning-list'),
    path('exam/<str:type>/', VocaTestCheckList.as_view(), name='voca-test-check-list'),
    path('exam/result', VocaTestResultList.as_view(), name='voca-test-result-list'),
]