from django.http import Http404
from rest_framework import status
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
