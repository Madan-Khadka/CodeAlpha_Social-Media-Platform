from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import (
    ProfileForm,
    RegisterForm,
    UserUpdateForm,
)

from .models import (
    Comment,
    Follow,
    Like,
    Post,
    PostImage,
)


# ============================================================
# PROFILE HELPER
# ============================================================

def get_profile(user):
    profile, created = user.profile.__class__.objects.get_or_create(
        user=user
    )

    return profile


# ============================================================
# HOME
# ============================================================

@login_required
def home(request):

    posts = (
        Post.objects
        .select_related("author")
        .prefetch_related(
            "images",
            "comments__author",
            "likes",
        )
        .all()
    )

    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list(
        "following_id",
        flat=True,
    )

    return render(
        request,
        "social/home.html",
        {
            "posts": posts,
            "following_ids": list(following_ids),
        },
    )


# ============================================================
# REGISTER
# ============================================================

def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            from .models import Profile

            Profile.objects.create(
                user=user
            )

            login(request, user)

            messages.success(
                request,
                "Welcome to SocialHub!",
            )

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "social/register.html",
        {
            "form": form,
        },
    )


# ============================================================
# LOGIN
# ============================================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        messages.error(
            request,
            "Invalid username or password.",
        )

    return render(
        request,
        "social/login.html",
    )


# ============================================================
# LOGOUT
# ============================================================

@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


# ============================================================
# CREATE POST
# ============================================================

@login_required
def create_post(request):

    if request.method != "POST":
        return redirect("home")

    content = request.POST.get(
        "content",
        ""
    ).strip()

    uploaded_images = request.FILES.getlist(
        "images"
    )

    if not content and not uploaded_images:

        messages.error(
            request,
            "Please write something or select a photo.",
        )

        return redirect("home")

    post = Post.objects.create(
        author=request.user,
        content=content,
    )

    # Save multiple selected images
    for image in uploaded_images:

        PostImage.objects.create(
            post=post,
            image=image,
        )

    messages.success(
        request,
        "Post published successfully.",
    )

    return redirect("home")


# ============================================================
# DELETE POST
# ============================================================

@login_required
@require_POST
def delete_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
    )

    if post.author != request.user:
        return JsonResponse(
            {
                "success": False,
                "message": "Permission denied.",
            },
            status=403,
        )

    post.delete()

    return JsonResponse(
        {
            "success": True,
        }
    )


# ============================================================
# LIKE / UNLIKE
# ============================================================

@login_required
@require_POST
def like_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
    )

    like = Like.objects.filter(
        post=post,
        user=request.user,
    ).first()

    if like:

        like.delete()
        liked = False

    else:

        Like.objects.create(
            post=post,
            user=request.user,
        )

        liked = True

    return JsonResponse(
        {
            "success": True,
            "liked": liked,
            "likes_count": post.likes.count(),
        }
    )


# ============================================================
# ADD COMMENT
# ============================================================

@login_required
@require_POST
def add_comment(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
    )

    text = request.POST.get(
        "text",
        ""
    ).strip()

    if not text:

        return JsonResponse(
            {
                "success": False,
                "message": "Comment cannot be empty.",
            },
            status=400,
        )

    comment = Comment.objects.create(
        post=post,
        author=request.user,
        text=text,
    )

    return JsonResponse(
        {
            "success": True,
            "comment": {
                "id": comment.id,
                "text": comment.text,
                "author": comment.author.username,
                "created_at": comment.created_at.strftime(
                    "%b %d, %Y %I:%M %p"
                ),
            },
            "comments_count": post.comments.count(),
        }
    )


# ============================================================
# PROFILE
# ============================================================

@login_required
def profile_view(request, username):

    clean_username = username.strip().lstrip("@")

    user = User.objects.filter(
        username__iexact=clean_username
    ).first()

    if not user:
        messages.error(
            request,
            "Account not found.",
        )

        return redirect("home")

    posts = (
        Post.objects
        .filter(author=user)
        .prefetch_related(
            "images",
            "comments__author",
            "likes",
        )
    )

    followers_count = Follow.objects.filter(
        following=user
    ).count()

    following_count = Follow.objects.filter(
        follower=user
    ).count()

    total_likes = Like.objects.filter(
        post__author=user
    ).count()

    is_following = False

    if request.user != user:

        is_following = Follow.objects.filter(
            follower=request.user,
            following=user,
        ).exists()

    return render(
        request,
        "social/profile.html",
        {
            "profile_user": user,
            "posts": posts,
            "followers_count": followers_count,
            "following_count": following_count,
            "total_likes": total_likes,
            "is_following": is_following,
        },
    )


# ============================================================
# EDIT PROFILE
# ============================================================

@login_required
def edit_profile(request):

    profile = get_profile(request.user)

    if request.method == "POST":

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user,
        )

        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )

        if (
            user_form.is_valid()
            and profile_form.is_valid()
        ):

            user_form.save()
            profile_form.save()

            messages.success(
                request,
                "Profile updated successfully.",
            )

            return redirect(
                "profile",
                username=request.user.username,
            )

    else:

        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        "social/edit_profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


# ============================================================
# FOLLOW / UNFOLLOW
# ============================================================

@login_required
@require_POST
def follow_user(request, username):

    clean_username = username.strip().lstrip("@")

    target_user = User.objects.filter(
        username__iexact=clean_username
    ).first()

    if not target_user:

        return JsonResponse(
            {
                "success": False,
                "message": "Account not found.",
            },
            status=404,
        )

    if target_user == request.user:

        return JsonResponse(
            {
                "success": False,
                "message": "You cannot follow yourself.",
            },
            status=400,
        )

    relationship = Follow.objects.filter(
        follower=request.user,
        following=target_user,
    ).first()

    if relationship:

        relationship.delete()
        following = False

    else:

        Follow.objects.create(
            follower=request.user,
            following=target_user,
        )

        following = True

    followers_count = Follow.objects.filter(
        following=target_user
    ).count()

    return JsonResponse(
        {
            "success": True,
            "following": following,
            "followers_count": followers_count,
        }
    )


# ============================================================
# FOLLOWERS LIST
# ============================================================

@login_required
def followers_view(request, username):

    clean_username = username.strip().lstrip("@")

    target_user = User.objects.filter(
        username__iexact=clean_username
    ).first()

    if not target_user:

        messages.error(
            request,
            "Account not found.",
        )

        return redirect("home")

    relationships = (
        Follow.objects
        .filter(following=target_user)
        .select_related("follower")
    )

    followers = [
        relationship.follower
        for relationship in relationships
    ]

    return render(
        request,
        "social/followers.html",
        {
            "profile_user": target_user,
            "users": followers,
            "title": "Followers",
        },
    )


# ============================================================
# FOLLOWING LIST
# ============================================================

@login_required
def following_view(request, username):

    clean_username = username.strip().lstrip("@")

    target_user = User.objects.filter(
        username__iexact=clean_username
    ).first()

    if not target_user:

        messages.error(
            request,
            "Account not found.",
        )

        return redirect("home")

    relationships = (
        Follow.objects
        .filter(follower=target_user)
        .select_related("following")
    )

    users = [
        relationship.following
        for relationship in relationships
    ]

    return render(
        request,
        "social/following.html",
        {
            "profile_user": target_user,
            "users": users,
            "title": "Following",
        },
    )


# ============================================================
# USER SEARCH
# ============================================================

@login_required
def search_users(request):

    query = request.GET.get(
        "q",
        ""
    ).strip()

    query_without_at = query.lstrip("@")

    users = User.objects.none()

    if query_without_at:

        users = (
            User.objects
            .filter(
                Q(username__icontains=query_without_at)
                | Q(first_name__icontains=query_without_at)
                | Q(last_name__icontains=query_without_at)
            )
            .exclude(
                id=request.user.id
            )
            .select_related("profile")
            .order_by("username")
        )

    return render(
        request,
        "social/search.html",
        {
            "query": query,
            "users": users,
        },
    )