from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, FlightSerializer, AtcSerializer, RunwaySerializer, NeighbourSerializer, PathSerializer, TakeoffSerializer, LandingSerializer, MessageSerializer
from flight.models import Flight, Path
from atc.models import Atc, Runway, Neighbour, Message
from queues.models import Takeoff, Landing


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class FlightViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class AtcViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Atc.objects.all()
    serializer_class = AtcSerializer


class RunwayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Runway.objects.all()
    serializer_class = RunwaySerializer


class PathViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Path.objects.all()
    serializer_class = PathSerializer


class NeighbourViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Neighbour.objects.all()
    serializer_class = NeighbourSerializer


class TakeoffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Takeoff.objects.all()
    serializer_class = TakeoffSerializer


class LandingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Landing.objects.all()
    serializer_class = LandingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



