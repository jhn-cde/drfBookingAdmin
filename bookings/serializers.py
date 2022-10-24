from pyexpat import model
from rest_framework import serializers
from .models import Booking, Contact, Tour, TourRegistry, Traveler, TravelerRegistry

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'docId', 'name', 'phone', 'email',)

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'price', 'outstanding', 'bookingDate', 'state', 'contactId')

class TravelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveler
        fields = ('id', 'docId', 'fNames', 'lNames', 'country', 'birth')

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('id', 'tour', 'price')

class TravelerRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelerRegistry
        fields = ('id', 'bookingId', 'travelerId')
class TourRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourRegistry
        fields = ('id', 'bookingId', 'tourId')