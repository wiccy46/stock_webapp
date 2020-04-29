from django.shortcuts import render

# from django_tables2 import SingleTableView
from dashboard.models import Summary
# from dashboard.tables import SummaryTable



def dashboard(request):
    return render(request, 'dashboard.html', {})


def prices(request):
    return render(request, 'prices.html', {})


def settings(request):
    return render(request, 'settings.html', {})

# class SummaryView(SingleTableView):
#     model = SummaryTable
#     table_class = SummaryTable
#     template_name = 'singtable.html'

def singletable(request):
    model = Summary
    field_names = [f.name for f in model._meta.get_fields()]
    data = [[getattr(ins, name) for name in field_names]
            for ins in model.objects.prefetch_related().all()]
    return render(request, 'singletable.html', {'field_names': field_names, 'data': data})