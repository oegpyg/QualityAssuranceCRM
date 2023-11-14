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
