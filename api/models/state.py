from django.db import models


class State(models.Model):
    abbreviation = models.CharField(max_length=2)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'states'
