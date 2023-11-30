from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views as AccountsViews
from blog import views as PostViews

router = DefaultRouter()
router.register("accounts", AccountsViews.UserViewSet)
router.register("blog", PostViews.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('blog/', include('blog.urls')),
]