from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):
    def get_context(self):
        return {}
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context=self.get_context())