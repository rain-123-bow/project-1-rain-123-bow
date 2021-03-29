from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("no_match", views.no_match, name="no_match"),
    path("create_newpage", views.create_newpage, name="create_newpage"),
    path("create/", views.create, name="create"),
    path("random_page", views.random_page, name="random_page"),
    path('<str:name>', views.show, name="show")
]
