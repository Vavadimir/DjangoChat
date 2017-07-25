from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Comments(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="username",
    )
    pub_date = models.DateTimeField('date published', primary_key=True)
    comment = models.CharField(max_length=200)

