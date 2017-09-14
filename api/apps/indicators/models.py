from django.db import models


class UF(models.Model):
    date = models.DateField(db_index=True, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'indicators_uf'
        ordering = ['date']

    class JSONAPIMeta:
        resource_name = 'uf'
