from typing import ClassVar

from django.http import Http404
from rest_framework import filters, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from project_setup.models import StreamPlatform
from serializers_views.api import serializers
from watchlist_app.models import Review, WatchList


class WatchlistBasicSerializerView(APIView):
    def get(self, request, format=None):
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        serializer = serializers.WatchlistSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        serializer = serializers.WatchlistSerializer(
            watchlist, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchlistBaseSerializerView(APIView):
    def get(self, request, format=None):
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistBaseSerializer(watchlist, many=True)
        return Response(serializer.data)


class WatchlistGAPIView(generics.GenericAPIView):
    queryset = WatchList.objects.all()
    serializer_class = serializers.WatchlistModelSerializer
    pagination_class = PageNumberPagination
    filter_backends: ClassVar = [filters.SearchFilter, filters.OrderingFilter]
    search_fields: ClassVar = ["title", "imdb_rating"]
    ordering_fields: ClassVar = ["title", "imdb_rating", "created"]

    def get_queryset(self):
        return WatchList.objects.filter(active=True).order_by("title")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.WatchlistModelSerializer
        elif self.request.method == "GET":
            return serializers.WatchlistModelBasicSerializer

    def get(self, request, *args, **kwargs):
        watchlist = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(watchlist)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["name"] = "TEST"
        return context


class WatchlistDetailGAPIView(generics.GenericAPIView):
    queryset = WatchList.objects.all()
    serializer_class = serializers.WatchlistModelSerializer
    lookup_field = "title"
    lookup_url_kwarg = "title"
    search_fields: ClassVar = ["title", "imdb_rating"]
    ordering_fields: ClassVar = ["title", "imdb_rating", "created"]

    def get_queryset(self):
        return WatchList.objects.filter(active=True)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        obj = generics.get_object_or_404(queryset, **filter_kwargs)
        return obj

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class WatchlistModelSerializerView(APIView):
    def get(self, request, format=None):
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistModelSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.WatchlistModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        serializer = serializers.WatchlistModelSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        serializer = serializers.WatchlistModelSerializer(
            watchlist, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchlistHMSerializerView(APIView):
    def get(self, request, format=None):
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistHMSerializer(
            watchlist, many=True, context={"request": request}
        )
        return Response(serializer.data)


class WatchlistDetailHMSerializerView(APIView):
    def get(self, request, pk, format=None):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.WatchlistHMSerializer(
            watchlist, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        serializer = serializers.WatchlistHMSerializer(
            watchlist, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        serializer = serializers.WatchlistHMSerializer(
            watchlist, data=request.data, partial=True, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformDetailHMSerializerView(APIView):
    def get(self, request, pk, format=None):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.StreamPlatformHMSerializer(
            platform, context={"request": request}
        )
        return Response(serializer.data)


class WatchlistListSerializerView(APIView):
    def get(self, request, format=None):
        watchlist = WatchList.objects.all()
        serializer = serializers.WatchlistDemoListSerializer(
            watchlist, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request, format=None):
        if type(request.data) is dict:
            serializer = serializers.WatchlistDemoListSerializer(
                data=request.data, many=False
            )
        else:
            serializer = serializers.WatchlistDemoListSerializer(
                data=request.data, many=True
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewBasicSerializerView(APIView):
    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializer = serializers.ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class StreamPlatformBasicSerializerView(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.StreamPlatformSerializer(platform)
        return Response(serializer.data)
