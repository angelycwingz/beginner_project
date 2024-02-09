from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class DbzView(TemplateView):
    template_name = "dbz.html"


class NarutoView(TemplateView):
    template_name = "naruto.html"


class OnePieceView(TemplateView):
    template_name = "onepiece.html"
