from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
count = 0
@register.filter
@stringfilter
def cut(val,sep):
    return val.split(sep)[3]

@register.filter(name='times') 
def times(number):
    return range(1,number+1)
