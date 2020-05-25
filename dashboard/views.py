from django.shortcuts import render
import os
# from django_tables2 import SingleTableView
from dashboard.models import Summary
# from dashboard.tables import SummaryTable
# from plotly.offline import plot
# from plotly.graph_objs import Scatter
from stockmanager import Ticker, Portfolio

CWD = os.path.dirname(os.path.abspath(__file__))

def dashboard(request):
    aapl = Ticker("AAPL")
    price_table = aapl.get_price()
    labels = price_table.index.to_list()
    labels = [s.strftime("%Y-%m-%d, %H:%M:%S") for s in labels]
    close_price = price_table.Close.to_list()
    close_price = [float(format(i, '.2f')) for i in close_price]

    # Load store data for portfoli
    my_portfolio = Portfolio()
    my_portfolio.load(summary_path=CWD + '/data/portfolio.csv',
                      record_path=CWD + '/data/records.csv')
    holdings = my_portfolio.summary.to_html()

    context = {'labels': labels,
                'close_price': close_price,
                'holdings': holdings}
    return render(request, 'dashboard.html', context=context)


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