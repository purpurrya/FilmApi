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
        "reviewlist-basic-serializer/",
        views.ReviewBasicSerializerView.as_view(),
        name="reviewlist-basic-serializer",
    ),
]
