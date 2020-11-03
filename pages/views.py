from django.views import generic



class ContactTemplateView(generic.TemplateView):
    template_name = 'contact.html'


class EkotermTemplateView(generic.TemplateView):
    template_name = 'ekoterm.html'


class EnvironmentTemplateView(generic.TemplateView):
    template_name = 'environment.html'


class FuelsTemplateView(generic.TemplateView):
    template_name = 'fuels.html'


class HistoryTemplateView(generic.TemplateView):
    template_name = 'history.html'


class HomePageTemplateView(generic.TemplateView):
    template_name = 'home.html'


class OilsTemplateView(generic.TemplateView):
    template_name = 'oils.html'


class PrivacyTemplateView(generic.TemplateView):
    template_name = 'privacy.html'


contact_view = ContactTemplateView.as_view()

ekoterm_view = EkotermTemplateView.as_view()

environment_view = EnvironmentTemplateView.as_view()

fuels_view = FuelsTemplateView.as_view()

history_view = HistoryTemplateView.as_view()

home_view = HomePageTemplateView.as_view()

oils_view = OilsTemplateView.as_view()

privacy_view = PrivacyTemplateView.as_view()
