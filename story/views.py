from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from auth.auth import IsNotMember
from story.models import Story
from story.serializers import StorySerializer

from common.serializers.generic_serializer import ResponseSerializer


class CMSStoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsNotMember]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = StorySerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        serializer = ResponseSerializer({
            'code': 201,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Story created successfully'
            },
            'error': None,
        })

        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StorySerializer(instance, data=request.data, partial=True)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Story updated successfully'
            },
            'error': None,
        })

        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        if request.query_params.get('id'):
            story = Story.objects.filter(id=request.query_params.get('id'))

            if not story.exists():
                raise NotFound('Story not found')

            story.delete()

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Story deleted successfully'
            },
            'error': None,
        })

        return Response(serializer.data, status=200)

    def list(self, request, *args, **kwargs):
        if request.query_params.get('id'):
            stories = Story.objects.filter(id=request.query_params.get('id'))

            if not stories.exists():
                raise NotFound('Story not found')

            serializer = ResponseSerializer({
                'code': 200,
                'status': 'success',
                'records_total': 1,
                'data': StorySerializer(stories.first()).data,
                'error': None,
            })

            return Response(serializer.data, status=200)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = StorySerializer(queryset, many=True)

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': queryset.count(),
            'data': serializer.data,
            'error': None,
        })

        return Response(serializer.data, status=200)

    def update_view_count(self, request, *args, **kwargs):
        story = self.get_object()
        story.reader_count += 1
        story.save()

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Story view count updated successfully'
            },
            'error': None,
        })

        return Response(serializer.data, status=200)

class PublicStoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.filter()
    serializer_class = StorySerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        if request.query_params.get('id'):
            stories = Story.objects.filter(id=request.query_params.get('id'))

            if not stories.exists():
                raise NotFound('Story not found')

            serializer = ResponseSerializer({
                'code': 200,
                'status': 'success',
                'records_total': 1,
                'data': StorySerializer(stories.first()).data,
                'error': None,
            })

            return Response(serializer.data, status=200)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = StorySerializer(queryset, many=True)

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': queryset.count(),
            'data': serializer.data,
            'error': None,
        })

        return Response(serializer.data, status=200)
