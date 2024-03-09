
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r"codes", views.CodeViewSet, basename="codes")
router.register(r"links", views.SharedLinkViewSet, basename="links")

urlpatterns = [
    path('admin/', admin.site.urls),
]+ router.urls
