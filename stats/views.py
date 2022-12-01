from django.shortcuts import render
from django.db.models import Max, Min

from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.embed import components
from bokeh.plotting import figure
import math


from stats.models import TempStat

# Create your views here.
def index(request):

    # things to go in the "home" page

    return render(request, 'index.html')


def line(request):
    
    max_year = TempStat.objects.aggregate(max_yr=Max('year'))['max_yr']
    min_year = TempStat.objects.aggregate(min_yr=Max('year'))['min_yr']

    tempdata = TempStat.objects.order_by('year')

    years =[d.year for d in tempdata]
    mean_temp =[d.annual_mean for d in tempdata]
    moving_mean=[d.moving_mean for d in tempdata]
    temp = [mean_temp, moving_mean]

    cds = ColumnDataSource(data=dict(years=years, moving_mean=moving_mean, mean_temp=mean_temp))

    fig = figure(height=500, title=f"Test Graph")
    fig.title.align = 'center'
    fig.title.text_font_size='1.5em'
    fig.xaxis.major_label_orientation = math.pi/4
    fig.yaxis[0].formatter = NumeralTickFormatter(format="0.0a")
    fig.yaxis.axis_label='Temperature [°C]'
    fig.xaxis.axis_label='Year'
    fig.axis.axis_label_text_font_size = '20px'
    fig.axis.axis_label_text_font_style = 'bold'
    

    fig.line(source=cds, x = 'years', y ='mean_temp', width=0.8)


    script, div = components(fig)

    context = {
        # 'annual_mean': annual_mean,
        'years': years,
        'script' : script,
        'div': div,
        'byears': range(1920, 2000),
        'pbyears': range(1860, 2000)

    }

    if request.htmx:
        return render(request, 'partials/temp-bar.html', context)

    return render(request, 'line.html', context)


