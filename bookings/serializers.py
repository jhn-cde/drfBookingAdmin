from pyexpat import model
from rest_framework import serializers
from .models import Booking, Contact, Tour, TourRegistry, Traveler, TravelerRegistry

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class TravelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveler
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class TravelerRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelerRegistry
        fields = '__all__'

class TourRegistrySerializer(serializers.ModelSerializer):
    tour = serializers.CharField(source='tourId.tour')
    price = serializers.FloatField(source='tourId.price')
    class Meta:
        model = TourRegistry
        fields = ['id', 'bookingId', 'tourId', 'tour', 'price']

class BookingSerializer(serializers.ModelSerializer):
    tours = TourRegistrySerializer(many=True, read_only=True)
    clientName = serializers.CharField(source='contactId.name')
    email = serializers.CharField(source='contactId.email')
    phone = serializers.CharField(source='contactId.phone')
    class Meta:
      model = Booking
      fields = ('id', 'state', 'contactId', 'departDate', 'clientName', 'email', 'phone', 'tours')