from django.views import generic


class HomePageTemplateView(generic.TemplateView):
    template_name = 'home.html'


class PhonesTemplateView(generic.TemplateView):
    template_name = 'phones.html'

home_view = HomePageTemplateView.as_view()

phones_view = PhonesTemplateView.as_view()
