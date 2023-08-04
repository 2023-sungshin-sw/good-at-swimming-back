from django.db import models


# 회원 모델
class User(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(null=False, max_length=20)
    phone = models.CharField(null=False, max_length=20)
    password = models.CharField(null=False, max_length=20)
