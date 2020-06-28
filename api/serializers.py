from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from content import models


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ('name',)


class AuthorSerializer(serializers.ModelSerializer):
    # Coding password
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class RecipeSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = models.Recipe
        fields = ('title', 'author', 'photo', 'ingredients')


class RecipeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ('title',)


class IngredientLineSerializer(serializers.ModelSerializer):
    recipe = RecipeNameSerializer()
    ingredient = IngredientSerializer()

    class Meta:
        model = models.IngredientLine
        fields = ('ingredient', 'quantity', 'unity', 'recipe')
