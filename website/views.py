from django.views.generic import ListView
from website.models import PrivacyPolicy, TermsAndConditions, FAQ

class PrivacyPolicyListView(ListView):
    model = PrivacyPolicy
    template_name = 'website/privacy_policy.html'
    context_object_name = 'privacy_policies'

class TermsAndConditionsListView(ListView):
    model = TermsAndConditions
    template_name = 'website/terms_and_conditions.html'
    context_object_name = 'terms_and_conditions'

class FAQListView(ListView):
    model = FAQ
    template_name = 'website/faq.html'
    context_object_name = 'faqs'