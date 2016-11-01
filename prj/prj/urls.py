from django.conf.urls import include, url
from django.contrib import admin
from product.views import product_list, product_simple, like, index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/$', product_list, name='product_list'),
    url(r'^products/(?P<slug>[\w-]+)/$', product_simple, name='product_simple'),
    url(r'^products/like/(?P<slug>[\w-]+)/$', like, name='like'),
    url(r'^$', index, name='index')
]
