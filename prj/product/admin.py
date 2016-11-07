# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Product, Comment, Like
from django.core.urlresolvers import reverse
from prj.settings.base import PORTAL_URL

# Register your models here.


class ProductInline(admin.TabularInline):
    """Add like to Product"""
    model = Like
    fieldsets = (
        (
            None,
            {
                'fields': ('user',)
            }
        ),
    )
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    """Product admin
    Set display fields in admin-panel.
    Set view on site
    """
    # exclude = ['slug']
    inlines = (ProductInline,)

    view_on_site = True  # True is default

    # def view_on_site(self, obj):
    #     url = reverse('product_simple', kwargs={'slug': obj.slug})
    #
    #     return PORTAL_URL + url


class CommentAdmin(admin.ModelAdmin):
    """Cooment admin
    Set display fields in admin-panel.
    """
    list_display = ['name', 'created_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
