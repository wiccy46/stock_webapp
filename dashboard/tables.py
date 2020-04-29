import django_tables2 as tables 
from .models import Summary

class SummaryTable(tables.Table):
    class Meta:
        model = Summary 