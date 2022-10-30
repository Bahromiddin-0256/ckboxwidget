from django.shortcuts import render
from django.views import generic
from main import forms
# Create your views here.


class IndexView(generic.CreateView):
    template_name = "index.html"
    form_class = forms.ArticleForm

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)

