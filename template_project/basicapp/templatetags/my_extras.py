from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """This removes spaces from the String"""
    return value.replace(arg,"")

# register.filter('cut',cut)