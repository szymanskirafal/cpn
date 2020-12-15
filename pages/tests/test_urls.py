import pytest
import requests

from django.views import generic
from django.urls import resolve, reverse

from ..views import HomePageTemplateView


@pytest.fixture(scope="class")
def url_resolved():
    return resolve('/')


class TestHomeUrl:

    def test_url_app_name(self, url_resolved):
        print(' ---- dir ----: ', dir(url_resolved))
        assert url_resolved.app_name == 'pages'

    def test_url_func_name(self, url_resolved):
        assert url_resolved.func.__name__ == 'HomePageTemplateView'

    def test_url_namespace(self, url_resolved):
        assert url_resolved.namespace == 'pages'

    def test_url_name(self, url_resolved):
        assert url_resolved.url_name == 'home'

    def test_url_view_name(self, url_resolved):
        assert url_resolved.view_name == 'pages:home'

"""

    def test_url_reverse(self):
        url_given = reverse('/')
        url_expected = '/'
        assert url_given == url_expected







"""
