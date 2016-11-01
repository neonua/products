# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, page, value):
    """Pagination tag. To avoid dropped parameters.
    Change url.
    """
    dict_ = request.GET.copy()
    dict_[page] = value
    return dict_.urlencode()
