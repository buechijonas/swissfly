from django.urls import path

from root.views import DisclaimerView, ImpressumView, PrivacyView, TermsView

urlpatterns = [
    path("impressum/", ImpressumView.as_view(), name="impressum"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
    path("terms/", TermsView.as_view(), name="terms"),
    path("disclaimer/", DisclaimerView.as_view(), name="disclaimer"),
]
