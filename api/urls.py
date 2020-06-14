from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = router.urls
