from django.urls import path
from .views import home_view, phones_view

app_name = "pages"
urlpatterns = [
    path(
        '',
        view = home_view,
        name = 'home',
    ),
    path(
        'phones/',
        view = phones_view,
        name = 'phones',
    ),

]
