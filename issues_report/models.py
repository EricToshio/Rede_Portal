from django.db import models
import uuid

# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=50)
    localization = models.CharField(max_length=5)
    iniciativa = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    ticket = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(default="enviado",max_length=20)