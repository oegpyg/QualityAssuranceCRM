from django import template

register = template.Library()


@register.filter
def count_by_status(value, by):
    return len(value.filter(status=by))


@register.filter
def count_by_status_perc(value, by):
    fil = len(value.filter(status=by))
    all_data = len(value.all())
    try:
        porc = (fil / all_data) * 100
    except ZeroDivisionError:
        porc = 0.0
    return porc


@register.filter
def color_by_status_perc(value, by):
    fil = len(value.filter(status=by))
    all_data = len(value.all())
    try:
        porc = (fil / all_data) * 100
    except ZeroDivisionError:
        porc = 0.0
    if 0.0 <= porc <= 25.9:
        return 'bg-primary'
    elif 26.0 <= porc <= 75.9:
        return 'bg-primary'
    elif int(porc) == 100:
        return 'bg-success'


@register.filter
def status_color(value):
    colors = ["", 'bg-secondary', 'bg-primary',
              'bg-warning', 'bg-info', 'bg-success']
    return colors[value]
