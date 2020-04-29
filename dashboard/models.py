from django.db import models

class Summary(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=20)
    exchange = models.CharField(max_length=20)
    price_at_registeration = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    currency = models.CharField(max_length=5)
    # Date = models.CharField(max_length=50)
    Date = models.DateField()

    class Meta:
        db_table = 'summary'
