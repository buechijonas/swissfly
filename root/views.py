from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()


# Create your views here.
class ImpressumView(TemplateView):
    model = User
    template_name = "pages/impressum.html"


class PrivacyView(TemplateView):
    model = User
    template_name = "pages/privacy.html"


class TermsView(TemplateView):
    model = User
    template_name = "pages/terms.html"


class DisclaimerView(TemplateView):
    model = User
    template_name = "pages/disclaimer.html"
