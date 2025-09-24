from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Get a value from a dictionary by key"""
    return dictionary.get(key) if dictionary else None

@register.filter
def timeuntil(value, arg):
    """Custom filter to calculate time between two dates"""
    from django.utils.timesince import timesince
    return timesince(arg, value)