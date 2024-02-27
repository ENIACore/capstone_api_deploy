from django.urls import include, path
from rest_framework import routers
from django.views.generic import RedirectView

from user import views as user_views
from trip import views as trip_views

router = routers.DefaultRouter()
router.register(r'users', user_views.ClientViewSet)
router.register(r'trips', trip_views.TripViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/v1/')),
    path('api/v1/', include(router.urls)),
    path('api/v1/login', user_views.LoginView.as_view(), name='account_login'),
    path('api/v1/logout', user_views.LogoutView.as_view(), name='account_logout'),
]

urlpatterns += router.urls
