from datetime import datetime
from django.db import models
# from simple_history.models import HistoricalRecords
# from simple_history.utils import update_change_reason
import reversion
# Create your models here.


class Products(models.Model):

    name = models.CharField(db_index=True, max_length=200)
    price = models.FloatField(default=0)
    address = models.CharField(max_length=200)
    # history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)
        reversion.set_comment('Add Product')
        # update_change_reason(self, 'Add Product')