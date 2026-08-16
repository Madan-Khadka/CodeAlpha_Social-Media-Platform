from django.contrib import admin

from .models import (
    Comment,
    Follow,
    Like,
    Post,
    PostImage,
    Profile,
)


# ============================================================
# PROFILE ADMIN
# ============================================================

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
    )


# ============================================================
# POST IMAGE ADMIN
# ============================================================

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):

    list_display = (
        "post",
        "created_at",
    )

    list_filter = (
        "created_at",
    )


# ============================================================
# POST ADMIN
# ============================================================

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "author",
        "total_likes",
        "total_comments",
        "created_at",
    )

    search_fields = (
        "author__username",
        "content",
    )

    list_filter = (
        "created_at",
    )

    def total_likes(self, obj):
        return obj.likes.count()

    total_likes.short_description = "Likes"

    def total_comments(self, obj):
        return obj.comments.count()

    total_comments.short_description = "Comments"


# ============================================================
# COMMENT ADMIN
# ============================================================

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "author",
        "post",
        "text",
        "created_at",
    )

    search_fields = (
        "author__username",
        "text",
    )

    list_filter = (
        "created_at",
    )


# ============================================================
# LIKE ADMIN
# ============================================================

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "post",
        "created_at",
    )

    search_fields = (
        "user__username",
    )


# ============================================================
# FOLLOW ADMIN
# ============================================================

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):

    list_display = (
        "follower",
        "following",
        "created_at",
    )

    search_fields = (
        "follower__username",
        "following__username",
    )