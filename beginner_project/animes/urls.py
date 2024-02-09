from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("dbz/", views.DbzView.as_view(), name="dbz"),
    path("naruto/", views.NarutoView.as_view(), name="naruto"),
    path("one_piece/", views.OnePieceView.as_view(), name="one_piece"),
]
