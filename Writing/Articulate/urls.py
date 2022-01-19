from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/<username>", views.profile, name="profile"),
    path("login/", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("explore", views.explore, name="explore"),
    path("logout/", views.logout_view, name="logout"),
    path("write/", views.write, name="write"),
    path("story_detail/<slug>", views.story_detail, name="story_detail"),
    path('see_story/', views.see_story, name="see_story"),
    path("update_story/<slug>", views.update_story, name="update_story"),
    path("delete_story/<id>", views.delete_story, name="delete_story"),
    path("edit_profile/", views.edit_profile, name="edit_profile")
]


urlpatterns += staticfiles_urlpatterns()