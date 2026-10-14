from django.db import models

class mesas(models.Model):
   numero_mesa = models.CharField(max_length=200)
   lugar = models.CharField(max_length=150)
   numero_sillas = models.DateField()

   def __str__(self):
       return self.numero_mesa
