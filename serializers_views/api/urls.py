from django.urls import path

from serializers_views.api import views

urlpatterns = [
    path(
        "watchlist-basic-serializer/",
        views.WatchlistBasicSerializerView.as_view(),
        name="watchlist-basic-serializer",
    ),
    path(
        "watchlist-basic-serializer/<int:pk>/",
        views.WatchlistBasicSerializerView.as_view(),
        name="watchlist-detail-basic-serializer",
    ),
    path(
        "watchlist-model-serializer/",
        views.WatchlistModelSerializerView.as_view(),
        name="watchlist-model-serializer",
    ),
    path(
        "watchlist-model-serializer/<int:pk>/",
        views.WatchlistModelSerializerView.as_view(),
        name="watchlist-detail-model-serializer",
    ),
    path(
        "wathclist-hm-serializer",
        views.WatchlistHMSerializerView.as_view(),
        name="wachlist-hm-serializer",
    ),
    path(
        "wathclist-detail-hm-serializer/<int:pk",
        views.WatchlistDetailHMSerializerView.as_view(),
        name="wachlist-detail-hm-serializer",
    ),
    path(
        "streamplatform-detail-hm-serializer",
        views.StreamPlatformDetailHMSerializerView.as_view(),
        name="Streamplatform-detail-hm-serializer",
    ),
    path(
        "reviewlist-basic-serializer/",
        views.ReviewBasicSerializerView.as_view(),
        name="reviewlist-basic-serializer",
    ),
]
