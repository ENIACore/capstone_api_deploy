from django.urls import include, path
from rest_framework import routers

from user import views

router = routers.DefaultRouter()
router.register(r'users', views.ClientViewSet)
router.register(r'login', views.LoginView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
