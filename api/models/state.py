from django.db import models

from django.db import models


# from uuid import uuid4
# Create your models here.

class State(models.Model):
    abbreviation = models.CharField(max_length=2)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'states'

# class Meta:
#    db_table = 'api'
# id = models.AutoField(primary_key=True)
# abbreviation = models.CharField(max_length=2, blank=False)
# name = models.CharField(max_length=100, blank=False)
# id = models.UUIDField(primary_key=True, default=uuid, editable=False)
