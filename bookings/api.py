from .models import Booking, Contact, Tour, TourRegistry, Traveler, TravelerRegistry
from rest_framework import viewsets, permissions
from .serializers import BookingSerializer, ContactSerializer, TourRegistrySerializer, TourSerializer, TravelerRegistrySerializer, TravelerSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookingSerializer

class TravelerViewSet(viewsets.ModelViewSet):
    queryset = Traveler.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TravelerSerializer

class TravelerRegistryViewSet(viewsets.ModelViewSet):
    queryset = TravelerRegistry.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TravelerRegistrySerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TourSerializer

class TourRegistryViewSet(viewsets.ModelViewSet):
    queryset = TourRegistry.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TourRegistrySerializer
