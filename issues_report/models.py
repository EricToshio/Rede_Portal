from django.db import models
from django.contrib.auth.models import User
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
    people_in_charge = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        return str(self.ticket)

