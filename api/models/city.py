from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    id_state = models.ForeignKey('State', on_delete=models.CASCADE, db_column='id_state')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cities'
