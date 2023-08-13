from django.db import models


# 회원 모델
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'user'