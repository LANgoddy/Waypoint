# Import Django's database model tools.
from django.db import models


# ---------------------------------------------------------
# PARK MODEL
# ---------------------------------------------------------

# This model stores information about a park.
class Park(models.Model):

    # Store the park name.
    name = models.CharField(max_length=100)

    # Store an optional description of the park.
    description = models.TextField(blank=True)

    # Display the park name when Django shows this object.
    def __str__(self):
        return self.name


# ---------------------------------------------------------
# TRAIL MODEL
# ---------------------------------------------------------

# This model stores information about a trail.
class Trail(models.Model):

    # Define the allowed trail difficulty values.
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("moderate", "Moderate"),
        ("hard", "Hard"),
        ("expert", "Expert"),
    ]

    # Connect each trail to one Park.
    park = models.ForeignKey(
        Park,
        on_delete=models.CASCADE,
        related_name="trails"
    )

    # Store the trail name.
    name = models.CharField(max_length=100)

    # Store the trail distance in kilometres.
    distance_km = models.FloatField()

    # Store the trail difficulty.
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES
    )

    # Store the elevation gained on the trail.
    elevation_gain_m = models.PositiveIntegerField()

    # Store whether the trail is currently open.
    # True means users can see it in the public trail catalogue.
    is_open = models.BooleanField(default=True)

    # Display the trail name when Django shows this object.
    def __str__(self):
        return self.name