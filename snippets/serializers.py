import logging
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICE
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

logger = logging.getLogger('test_django')


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError('Title is empty.')
        if value == 'error':
            raise serializers.ValidationError('Title is error.')
        return value


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')