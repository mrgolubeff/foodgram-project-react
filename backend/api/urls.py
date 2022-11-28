from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import TagViewSet, IngredientViewSet, RecipeViewSet, SubscribeListView, SubscribeCreateDestroyView, ShoppingCartView, FavoriteView

router = DefaultRouter()

router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')
# router.register('users/subscriptions', SubscribeListView, basename='user_subscriptions')

urlpatterns = [
    path(
        'users/<int:id>/subscribe/',
        SubscribeCreateDestroyView.as_view()
    ),
    path('users/subscriptions/',
         SubscribeListView.as_view(),
         name='subscriptions'),
    path('recipes/<int:id>/shopping_cart/',
         ShoppingCartView.as_view(),
         name='shopping_cart'),
    path('recipes/<int:id>/favorite/',
         FavoriteView.as_view(),
         name='favorite'),
    # path('recipes/download_shopping_cart/',

    # )
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
