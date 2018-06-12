from django.conf.urls import url, include
from rest_framework import routers
from api import views
from api.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'preferences', views.PreferenceViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'supplier_ratings', views.SupplierRatingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]