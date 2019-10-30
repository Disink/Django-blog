from . import views
from django.urls import path

from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #path('api-auth/', include('rest_framework.urls'), name='rset_framework')
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
