from django.views import generic


class HomePageTemplateView(generic.TemplateView):
    template_name = 'home.html'


class ContactTemplateView(generic.TemplateView):
    template_name = 'contact.html'

home_view = HomePageTemplateView.as_view()

contact_view = ContactTemplateView.as_view()
