from django import template

register = template.Library()

@register.filter
def sum_tables(total):
    result = 0
    result += total
    yield result