from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    """
    Representa Habitaciones para ser gestionado en el sistema.
    campos:
    - name: nombre de la habitación
    - description: descripción de la habitación
    - price_per_night: precio por noche en USD
    - is_available: indica si la habitación está disponible
    """

    name = models.CharField(max_length=100, help_text="Nombre de la habitación")
    description = models.TextField(
        max_length=100, help_text="Descripción de la habitación"
    )
    price_per_night = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="Precio por noche en USD"
    )
    is_available = models.BooleanField(
        default=True, help_text="Indica si la habitación está disponible"
    )

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """
    Representa una reserva de una habitación por un usuario.
    campos:
    - user (int): usuario que realiza la reserva
    - room (int): habitación reservada
    - start_date: fecha de inicio de la reserva
    - end_date: fecha de fin de la reserva
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="ID del Usuario que realiza la reserva",
    )
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, help_text="ID de la habitación reservada"
    )
    start_date = models.DateField(help_text="Fecha de inicio de la reserva")
    end_date = models.DateField(help_text="Fecha de fin de la reserva")

    def __str__(self):
        return f"{self.user.username} - {self.room.name}"
