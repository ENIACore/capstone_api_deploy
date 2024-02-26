from django.urls import include, path
from rest_framework import routers
from django.views.generic import RedirectView

from user import views

router = routers.DefaultRouter()
router.register(r'users', views.ClientViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/v1/')),
    path('api/v1/', include(router.urls)),
    path('api/v1/login', views.LoginView.as_view(), name='account_login'),
    path('api/v1/logout', views.LogoutView.as_view(), name='account_logout'),
]

urlpatterns += router.urls
