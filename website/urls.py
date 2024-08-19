from django.urls import path
from .views import (
    PrivacyPolicyListView,
    TermsAndConditionsListView,
    FAQListView
)

urlpatterns = [
    path('privacy-policies/', PrivacyPolicyListView.as_view(), name='privacy_policy'),
    path('terms-and-conditions/', TermsAndConditionsListView.as_view(), name='terms_and_conditions'),
    path('faqs/', FAQListView.as_view(), name='faqs'),
]
