import pytest
import requests

from django.views import generic

from ..views import HomePageTemplateView

def test_home_view():
    # arrange
    view = HomePageTemplateView()
    view_class_expected = generic.TemplateView
    view_template_name_expected = 'home.html'
    # act
    view_class_given = view.__class__.__base__
    view_template_name_given = view.template_name
    # assert
    assert view_class_given == view_class_expected
    assert view_template_name_given == view_template_name_expected
