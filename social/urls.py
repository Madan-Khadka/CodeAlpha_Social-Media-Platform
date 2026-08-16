from django.urls import path

from . import views


urlpatterns = [

    # ========================================================
    # HOME
    # ========================================================

    path(
        "",
        views.home,
        name="home",
    ),

    # ========================================================
    # AUTHENTICATION
    # ========================================================

    path(
        "register/",
        views.register_view,
        name="register",
    ),

    path(
        "login/",
        views.login_view,
        name="login",
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout",
    ),

    # ========================================================
    # POSTS
    # ========================================================

    path(
        "post/create/",
        views.create_post,
        name="create_post",
    ),

    path(
        "post/<int:post_id>/delete/",
        views.delete_post,
        name="delete_post",
    ),

    path(
        "post/<int:post_id>/like/",
        views.like_post,
        name="like_post",
    ),

    path(
        "post/<int:post_id>/comment/",
        views.add_comment,
        name="add_comment",
    ),

    # ========================================================
    # PROFILE
    # IMPORTANT: edit route BEFORE username route
    # ========================================================

    path(
        "profile/edit/",
        views.edit_profile,
        name="edit_profile",
    ),

    path(
        "profile/<str:username>/followers/",
        views.followers_view,
        name="followers",
    ),

    path(
        "profile/<str:username>/following/",
        views.following_view,
        name="following",
    ),

    path(
        "profile/<str:username>/follow/",
        views.follow_user,
        name="follow_user",
    ),

    path(
        "profile/<str:username>/",
        views.profile_view,
        name="profile",
    ),

    # ========================================================
    # SEARCH
    # ========================================================

    path(
        "search/",
        views.search_users,
        name="search",
    ),
]