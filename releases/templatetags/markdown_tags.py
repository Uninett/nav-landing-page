from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

import markdown as markdown_module

register = template.Library()


@register.filter(name="markdown")
def markdown_filter(text):
    return mark_safe(markdown_module.markdown(text, extensions=settings.MARKDOWN_EXTENSIONS))
markdown_filter.is_safe = True