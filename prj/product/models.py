# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.db import IntegrityError, transaction
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Product(models.Model):
    """Product model"""
    name = models.CharField(
        max_length=64,
        verbose_name=u'Name',
        blank=True
    )

    slug = models.SlugField(
        max_length=64,
        unique=True
    )

    description = models.TextField(
        verbose_name=u'Description'
    )

    price = models.FloatField(
        verbose_name=u'Price'
    )

    created_at = models.DateTimeField(
        default=datetime.datetime.now,
        editable=False,
        null=True
    )

    modified_at = models.DateTimeField(
        default=datetime.datetime.now,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return '{0}'.format(self.name)

    class Meta(object):
        verbose_name = u'Product'
        verbose_name_plural = u'Products'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        try:
            with transaction.atomic():
                super(Product, self).save(*args, **kwargs)
        except IntegrityError:
            self.slug = slugify(str(Product.objects.latest('id').id) + ' ' + self.name)

        if self.id:
            self.modified_at = datetime.datetime.now()
        else:
            self.created_at = datetime.datetime.now()
        super(Product, self).save(*args, **kwargs)


class Comment(models.Model):
    """Comment model"""
    product = models.ForeignKey(
        Product,
        verbose_name=u'Product',
    )

    name = models.CharField(
        verbose_name=u'Username',
        max_length=128
    )

    body = models.TextField(
        verbose_name=u'Comment'
    )

    created_at = models.DateTimeField(
        default=datetime.datetime.now,
        editable=False
    )

    def __unicode__(self):
        return '{0}'.format(self.name)

    class Meta(object):
        verbose_name = u'Comment'
        verbose_name_plural = u'Comments'


class Like(models.Model):
    """Like model"""
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0} liked'.format(self.user)

    class Meta(object):
        verbose_name = u'Who liked'
        verbose_name_plural = u'Who liked'
