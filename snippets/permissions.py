import logging
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

logger = logging.getLogger('test_django')


class SnippetPermission(permissions.IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        return super(SnippetPermission, self).has_permission(request, view)