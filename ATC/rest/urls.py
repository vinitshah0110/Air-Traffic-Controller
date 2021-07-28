from django.urls import include, path
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('flights', views.FlightViewSet)
router.register('atcs', views.AtcViewSet)
router.register('runways', views.RunwayViewSet)
router.register('paths', views.PathViewSet)
router.register('nears', views.NeighbourViewSet)
router.register('takeoffs', views.TakeoffViewSet)
router.register('landings', views.LandingViewSet)
router.register('messages', views.MessageViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]