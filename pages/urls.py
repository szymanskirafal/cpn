from django.urls import path
from .views import (
    home_view,
    about_view,
    contact_view,
    ekoterm_view,
    environment_view,
    fuels_view,
    history_view,
    oils_view,
    privacy_view,
    )

app_name = "pages"
urlpatterns = [
    path(
        '',
        view = home_view,
        name = 'home',
    ),
    path(
        'about/',
        view = about_view,
        name = 'about',
    ),
    path(
        'contact/',
        view = contact_view,
        name = 'contact',
    ),
    path(
        'ekoterm/',
        view = ekoterm_view,
        name = 'ekoterm',
    ),
    path(
        'environment/',
        view = environment_view,
        name = 'environment',
    ),
    path(
        'fuels/',
        view = fuels_view,
        name = 'fuels',
    ),
    path(
        'history/',
        view = history_view,
        name = 'history',
    ),
    path(
        'oils/',
        view = oils_view,
        name = 'oils',
    ),
    path(
        'privacy/',
        view = privacy_view,
        name = 'privacy',
    ),


]
