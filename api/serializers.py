from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from content import models


class AuthorSerializer(serializers.ModelSerializer):
    # Coding password
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ('title', 'author', 'photo')
