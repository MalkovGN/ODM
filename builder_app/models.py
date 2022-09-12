from django.contrib.auth.models import User
from django.db import models


class TableInfo(models.Model):

    values = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
