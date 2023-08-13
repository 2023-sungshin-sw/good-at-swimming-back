from django.db import models
from user.models import User


# 딘어 모델
class Vocabulary(models.Model):
    voca_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    word = models.CharField(max_length=20)
    meaning = models.CharField(max_length=20)
    example_en = models.CharField(max_length=100, blank=True, null=True)
    example_kr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vocabulary'


class Exam(models.Model):
    exam_id = models.BigAutoField(primary_key=True)
    voca = models.ForeignKey(Vocabulary, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exam'