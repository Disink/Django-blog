from . import views
from django.urls import path

from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),
    path('api/', include(router.urls)),
]
