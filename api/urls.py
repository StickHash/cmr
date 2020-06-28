from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'ingredients',views.IngredientLineViewSet)

urlpatterns = router.urls
