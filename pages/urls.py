from django.urls import path
from .views import home_view, contact_view

app_name = "pages"
urlpatterns = [
    path(
        '',
        view = home_view,
        name = 'home',
    ),
    path(
        'contact/',
        view = contact_view,
        name = 'contact',
    ),

]
