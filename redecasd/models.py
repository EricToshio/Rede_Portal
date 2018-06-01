from django.db import models

# Create your models here.
class ReservationRede(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=5)
    details = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    reservation_date = models.DateTimeField()
    status = models.CharField(default="pendente", max_length=20)
    # def __str__(self):
    #     return str(self.ticket)
