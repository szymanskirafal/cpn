from django.views import generic


class HomePageTemplateView(generic.TemplateView):
    template_name = 'home.html'

home_view = HomePageTemplateView.as_view()
