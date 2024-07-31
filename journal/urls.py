from django.urls import path

from journal.views import JournalViewSet

urlpatterns_journal = [
    path('', JournalViewSet.as_view({'get': 'list', 'post': 'create', 'patch': 'update', 'delete': 'destroy'}), name='cms-journal-list'),
]