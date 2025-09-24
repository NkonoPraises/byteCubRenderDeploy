from django import template
import re
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def get_display_name(value):
    """
    Extracts the display name from an HTML list item string.
    Example: '<a href="{% url 'link_name' %}"><li class="class name"> Some name </li></a>' -> 'Some name'
    """
    # A more robust regex to find content between <li> tags
    match = re.search(r'<li[^>]*>(.*?)</li>', value, re.DOTALL)
    if match:
        # Use strip_tags to remove any inner HTML if present
        return strip_tags(match.group(1)).strip()
    return "No display name found"

@register.filter
def get_link_url(value):
    """
    Extracts the URL name from an HTML string.
    Example: '<a href="{% url 'link_name' %}">' -> "link_name"
    """
    # A more robust regex to find the url name
    match = re.search(r"url\s+'([a-zA-Z0-9_]+)'", value)
    if match:
        return match.group(1)
    return ""