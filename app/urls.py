from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('image', views.PostImageViewSet, basename='product-images')

urlpatterns = [
    path('', include(router.urls)),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh")
]