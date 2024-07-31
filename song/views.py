from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from auth.auth import IsNotMember
from .models import Genre, Song
from .serializers import GenreSerializer, SongSerializer

from common.serializers.generic_serializer import ResponseSerializer

class CMSGenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsNotMember]

    def create(self, request, *args, **kwargs):
        serializer = GenreSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        response_serializer = ResponseSerializer({
            'code': 201,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Genre created successfully'
            },
            'error': None,
        })

        return Response(response_serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GenreSerializer(instance, data=request.data, partial=True)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        response_serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Genre updated successfully'
            },
            'error': None,
        })

        return Response(response_serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        response_serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Genre deleted successfully'
            },
            'error': None,
        })

        return Response(response_serializer.data, status=200)

    def list(self, request, *args, **kwargs):
        if request.query_params.get('id'):
            genres = Genre.objects.filter(id=request.query_params.get('id'))

            if not genres.exists():
                raise NotFound('Genre not found')

            response_serializer = ResponseSerializer({
                'code': 200,
                'status': 'success',
                'records_total': 1,
                'data': GenreSerializer(genres.first()).data,
                'error': None,
            })

            return Response(response_serializer.data, status=200)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = GenreSerializer(queryset, many=True)

        response_serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': queryset.count(),
            'data': serializer.data,
            'error': None,
        })

        return Response(response_serializer.data, status=200)


class CMSSongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsNotMember]

    def create(self, request, *args, **kwargs):
        serializer = SongSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        response_serializer = ResponseSerializer({
            'code': 201,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Song created successfully'
            },
            'error': None,
        })

        return Response(response_serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SongSerializer(instance, data=request.data, partial=True)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        response_serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Song updated successfully'
            },
            'error': None,
        })

        return Response(response_serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        response_serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Song deleted successfully'
            },
            'error': None,
        })

        return Response(response_serializer.data, status=200)

    def list(self, request, *args, **kwargs):
        if request.query_params.get('id'):
            songs = Song.objects.filter(id=request.query_params.get('id'))

            if not songs.exists():
                raise NotFound('Song not found')

            response_serializer = ResponseSerializer({
                'code': 200,
                'status': 'success',
                'records_total': 1,
                'data': SongSerializer(songs.first()).data,
                'error': None,
            })

            return Response(response_serializer.data, status=200)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = SongSerializer(queryset, many=True)

        response_serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': queryset.count(),
            'data': serializer.data,
            'error': None,
        })

        return Response(response_serializer.data, status=200)


class PublicGenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = GenreSerializer(queryset, many=True)

        response_serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': queryset.count(),
            'data': serializer.data,
            'error': None,
        })

        return Response(response_serializer.data, status=200)

class PublicSongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = SongSerializer(queryset, many=True)

        response_serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': queryset.count(),
            'data': serializer.data,
            'error': None,
        })

        return Response(response_serializer.data, status=200)