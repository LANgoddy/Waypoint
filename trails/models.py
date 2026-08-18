# Import Django's model tools.
from django.db import models


# ---------------------------------------------------------
# PARK MODEL
# ---------------------------------------------------------

# A Park represents a location that can contain many trails.
class Park(models.Model):

    # Store the park name.
    name = models.CharField(max_length=100)

    # Store an optional description of the park.
    description = models.TextField(blank=True)

    # Display the park name in Django Admin and the Django shell.
    def __str__(self):
        return self.name


# ---------------------------------------------------------
# TRAIL MODEL
# ---------------------------------------------------------

# A Trail represents a trail stored in the database.
class Trail(models.Model):

    # Difficulty choices help keep database values consistent.
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("moderate", "Moderate"),
        ("hard", "Hard"),
        ("expert", "Expert"),
    ]

    # Each trail belongs to one Park.
    # A Park can therefore contain many Trail records.
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

    # Store the elevation gain in metres.
    elevation_gain_m = models.PositiveIntegerField()

    # Display the trail name in Django Admin and the Django shell.
    def __str__(self):
        return self.name