from django.db import models


class UF(models.Model):
    date = models.DateField(db_index=True, unique=True)
    value = models.FloatField(default=0)
    created_ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'indicators_uf'
        ordering = ['date']

    class JSONAPIMeta:
        resource_name = 'uf'
