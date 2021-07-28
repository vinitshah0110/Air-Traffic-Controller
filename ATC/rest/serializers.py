from django.contrib.auth.models import User, Group
from rest_framework import serializers
from flight.models import Flight, Path
from atc.models import Atc, Runway, Neighbour, Message
from queues.models import Takeoff, Landing


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['name', 'starting_atc', 'ending_atc', 'starting_time', 'expected_end', 'path', 'distance', 'landing_type', 'states']


class AtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atc
        fields = '__all__'

class RunwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Runway
        fields = '__all__'


class NeighbourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbour
        fields = '__all__'


class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = '__all__'


class TakeoffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Takeoff
        fields = '__all__'

class LandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

