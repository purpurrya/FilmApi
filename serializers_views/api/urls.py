from django.urls import path

from serializers_views.api import views

urlpatterns = [
    path(
        "watchlist-basic-serializer/",
        views.WatchlistBasicSerializerView.as_view(),
        name="watchlist-basic-serializer",
    ),
    path(
        "review-basic-serializer/",
        views.ReviewBasicSerializerView.as_view(),
        name="review-basic-serializer",
    ),
    path(
        "stream-platform-basic-serializer/<int:pk>/",
        views.StreamPlatformBasicSerializerView.as_view(),
        name="streamplatform-detail-basic-serializer",
    ),
]
