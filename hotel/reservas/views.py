from rest_framework import viewsets
from .models import Reservation, Room
from .serializers import ReservationSerializer, RoomSerializer


# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    """
    ViewSet para la gestión de habitaciones.
    Metodos:
    - GET `api/rooms/`: lista todas las habitaciones
    - POST `api/rooms/`: crea una nueva habitación
    - GET `api/rooms/{id}/`: muestra una habitación por id
    - PUT `api/rooms/{id}/`: actualiza una habitación por id
    - DELETE `api/rooms/{id}/`: elimina una habitación por id
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    ViewSet para la gestión de reservas.
    Metodos:
    - GET `api/reservations/`: lista todas las reservas
    - POST `api/reservations/`: crea una nueva reserva
    - GET `api/reservations/{id}/`: muestra una reserva por id
    - PUT `api/reservations/{id}/`: actualiza una reserva por id
    - DELETE `api/reservations/{id}/`: elimina una reserva por id
    """

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
