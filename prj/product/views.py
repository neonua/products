# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, get_list_or_404
from .models import Product, Comment, Like
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from forms import CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib import messages
import json

# Create your views here.


def index(request):
    """Simple redirect to products list"""
    return redirect('product.views.product_list')


def product_list(request):
    """Return all products whith ordering and pagination
    Possibility to sorting from number of likes current page.
    """
    products = Product.objects.all().values('name', 'price',
                                            'description', 'slug'
                                            ).annotate(dcount=Count('like'))  # get values of products and count likes

    # order
    order_by = request.GET.get('order_by')
    if order_by in ('like',):
        products = products.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            products = products.reverse()

    # pagination
    page_products_count = 5  # items per gage
    paginator = Paginator(products,
                          page_products_count)
    page = request.GET.get('page')  # get value 'page' from request
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)  # if value 'page' not integer - set 'page' = 1
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # if value 'page' is out of range - set last page

    return render(request, 'product_all.html', {'products': products})


def product_simple(request, slug):
    """Return one current product. Identificated from slug.
    Get comments for current page with the time to display and ordering.
    Posting comment to the current page (no auth)
    Get and like.
    """
    product = get_object_or_404(Product, slug=slug)  # get product from slud-id

    # get list of comments
    hours_from = 24  # set time for showing comments on product page
    date_from = timezone.now() - timedelta(hours=hours_from)  # get date with a period of time comments are displayed
    comment = Comment.objects.filter(product__slug=slug, created_at__gte=date_from) \
        .order_by('-created_at').values('name', 'created_at', 'body')

    # like
    like = Like.objects.filter(product__slug=slug).count()  # get numbers of like current page
    user_likes_this = product.like_set.filter(user=request.user)  # liked or not from auth-user

    # Post comments
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            messages.success(request, "Comment add")  # django.message
            return redirect('product.views.product_simple', slug=product.slug)
    else:
        form = CommentForm()

    data = {
        'product': product,
        'comment': comment,
        'like': like,
        'user_likes_this': user_likes_this,
        'form': form
        }

    return render(request, 'product_simple.html', data)


@require_http_methods(["POST"])
def like(request, slug):
    """Func from add like for current page.
    Only auth-user.
    Only POST-method.
    And only ajax.
    """
    user = request.user  # current user
    ajax = {}
    if user.is_authenticated() and request.is_ajax():
        like, create = Like.objects.get_or_create(user=user, product=Product.objects.get(slug=slug))
        if create:
            like_prod = Like.objects.filter(product__slug=slug).count()  # return numbers of likes
            ajax['like_prod'] = like_prod
            return HttpResponse(json.dumps(ajax), content_type='application/json')
