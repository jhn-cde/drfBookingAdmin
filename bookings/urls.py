from rest_framework import routers

from .api import BookingViewSet, ContactViewSet, TourRegistryViewSet, TourViewSet, TravelerRegistryViewSet, TravelerViewSet

router = routers.DefaultRouter()

router.register('api/bookings', BookingViewSet, 'bookings')
router.register('api/contacts', ContactViewSet, 'contacts')
router.register('api/travelers', TravelerViewSet, 'travelers')
router.register('api/travelersreg', TravelerRegistryViewSet, 'travelersreg')
router.register('api/tours', TourViewSet, 'tours')
router.register('api/toursreg', TourRegistryViewSet, 'toursreg')

urlpatterns = router.urls

