"""Just some utility templatetags and filters for html encoding/decoding"""

from django import template
import HTMLParser

register = template.Library()


@register.filter
def decode_html(value):
    """HTML decodes a string """
    html_parser = HTMLParser.HTMLParser()
    return html_parser.unescape(value)
