from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all_devposts, name="get_devposts"),
    path("get_posts", views.get_posts_from_scraper, name="get_devposts_from_scraper")
]