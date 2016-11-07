from django.utils import timezone
from django.test import TestCase
from django.test.client import Client
from datetime import timedelta
from .models import Product, Comment, Like

# Create your tests here.


class ProductMethodTests(TestCase):

    fixtures = ["demo1.json"]

    def test_product_slug(self):
        """
        Check correct and incorrect slug product.
        If correct - get 200.
        Else - 404.
        """

        client = Client()
        slug = ['bryan-fox-snowboard-2017', 'some_slug']  # Correct and incorrect slug
        response = client.get('/products/{0}/'.format(slug[0]))
        self.assertEqual(response.status_code, 200)
        response = client.get('/products/{0}/'.format(slug[1]))
        self.assertEqual(response.status_code, 404)

    def test_like(self):
        """
        Get the number of likes and
        check for the possibility to like post
        """
        client = Client()
        slug = ['bryan-fox-snowboard-2017', 'some_slug']  # Correct and incorrect slug
        response = client.get('/products/{0}/'.format(slug[0]))
        self.assertEqual(response.status_code, 200)
        Like.objects.filter(product__slug=slug).count()  # numbers like of post
        product = Product.objects.get(slug=slug[0])
        if response.context["user"].is_authenticated():
            product.like_set.filter(user=response.context["user"])

    def test_comment(self):
        """
        Get the number of likes and
        check for the possibility to like post
        """
        slug = ['bryan-fox-snowboard-2017', 'some_slug']
        hours_from = 24
        date_from = timezone.now() - timedelta(hours=hours_from)
        Comment.objects.filter(product__slug=slug[0], created_at__gte=date_from) \
            .order_by('-created_at').values('name', 'created_at', 'body')

    def test_comment_post(self):
        """
        Test comment post
        """
        client = Client()
        slug = ['bryan-fox-snowboard-2017', 'some_slug']
        form_data = {'name': 'something', 'body': 'some text'}
        response = client.post('/products/{0}/'.format(slug[0]), form_data)
        self.assertEqual(response.status_code, 302)
