from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comment"
)
router.register(
    "follow", FollowViewSet, basename="follow"
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
