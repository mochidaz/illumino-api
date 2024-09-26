from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.serializers.generic_serializer import ResponseSerializer
from journal.models import Journal
from journal.serializers import JournalSerializer


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = JournalSerializer(data=request.data)

        serializer.user = request.user

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        serializer = ResponseSerializer({
            'code': 201,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Journal created successfully'
            },
            'error': None,
        })

        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = JournalSerializer(instance, data=request.data, partial=True)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Journal updated successfully'
            },
            'error': None,
        })

        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        if request.query_params.get('id'):
            journal = Journal.objects.filter(id=request.query_params.get('id'))

            if not journal.exists():
                raise NotFound('Journal not found')

            journal.delete()

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': {
                'message': 'Journal deleted successfully'
            },
            'error': None,
        })

        return Response(serializer.data, status=200)

    def list(self, request, *args, **kwargs):
        if request.query_params.get('id'):
            journals = Journal.objects.filter(id=request.query_params.get('id'))

            if not journals.exists():
                raise NotFound('Journal not found')

            journal_serializer = JournalSerializer(journals)

            serializer = ResponseSerializer({
                'code': 200,
                'status': 'success',
                'records_total': 1,
                'data': journal_serializer.data,
                'error': None,
            })

            return Response(serializer.data)

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(author=request.user)

        journal_serializer = JournalSerializer(queryset, many=True)

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': queryset.count(),
            'data': journal_serializer.data,
            'error': None,
        })

        return Response(serializer.data)