from django import template

from sol.models import Position

register = template.Library()

@register.filter(name='num_aba')
def num_aba(d, artist):
    return d[artist]

@register.filter(name='filter_by_chart')
def filter_by_chart(name):
    positions = Position.objects.filter(chart=name)
    return positions

@register.filter(name='filter_by_album')
def filter_by_album(name):
    positions = Position.objects.filter(album=name)
    return positions