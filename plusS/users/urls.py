from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet,basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]