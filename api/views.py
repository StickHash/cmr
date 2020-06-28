from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from api import serializers
from content import models


class RecipeViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AuthorViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = models.User.objects.filter(is_superuser=False)
    serializer_class = serializers.AuthorSerializer


class IngredientLineViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    queryset = models.IngredientLine.objects.all()
    serializer_class = serializers.IngredientLineSerializer