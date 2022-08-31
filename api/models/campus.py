from django.db import models


class Campus(models.Model):
    name = models.CharField(max_length=100)
    id_city = models.ForeignKey('City', models.DO_NOTHING, db_column='id_city')

    class Meta:
        managed = False
        db_table = 'campus'
