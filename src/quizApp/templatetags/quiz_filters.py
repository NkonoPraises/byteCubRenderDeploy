from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='preserve_formatting')
def preserve_formatting(text):
    """
    Preserves line breaks and spacing, and safely escapes HTML.
    """
    # Escape HTML, then convert line breaks to <br>
    escaped_text = conditional_escape(text)
    line_breaked_text = escaped_text.replace('\n', '<br>')
    return mark_safe(line_breaked_text)

from django import template

register = template.Library()



