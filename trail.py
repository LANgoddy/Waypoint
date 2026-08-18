# Import the Distance class so that each Trail object can store a Distance object.
from distance import Distance


# This class represents a trail in the Waypoint application.
# Each trail has an id, name, distance, elevation gain, and difficulty.
class Trail:

    # This class variable stores the default distance unit used by the platform.
    default_unit = "km"

    # These are the only difficulty values allowed in the application.
    ALLOWED_DIFFICULTIES = ("easy", "moderate", "hard", "expert")

    # The __init__ method runs automatically when a Trail object is created.
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty):

        # Store the trail id.
        self.id = trail_id

        # Store the trail name.
        self.name = name

        # If the distance passed in is already a Distance object,
        # store it directly.
        if isinstance(distance, Distance):
            self.distance = distance

        # Otherwise, create a new Distance object using the current default unit.
        else:
            self.distance = Distance(distance, Trail.default_unit)

        # Elevation gain cannot be negative.
        if elevation_gain_m < 0:
            raise ValueError("Elevation gain cannot be negative.")

        # Store the elevation gain.
        self.elevation_gain_m = elevation_gain_m

        # Difficulty is stored as private/internal state.
        self._difficulty = None

        # Use the setter method so difficulty is validated before being stored.
        self.set_difficulty(difficulty)

    # This method safely changes the difficulty of a trail.
    def set_difficulty(self, difficulty):

        # Use the static validator to check if the difficulty is allowed.
        if not Trail.is_valid_difficulty(difficulty):
            raise ValueError(
                "Difficulty must be easy, moderate, hard, or expert."
            )

        # Store the validated difficulty.
        self._difficulty = difficulty

    # Provide read-only access to the difficulty value.
    @property
    def difficulty(self):
        return self._difficulty

    # This static method checks whether a difficulty value is valid.
    # It does not need access to a specific Trail object.
    @staticmethod
    def is_valid_difficulty(difficulty):
        return difficulty in Trail.ALLOWED_DIFFICULTIES

    # This static method checks whether an elevation value is valid.
    @staticmethod
    def is_valid_elevation(elevation_gain_m):
        return elevation_gain_m >= 0

    # This class method changes the platform's default distance unit.
    @classmethod
    def set_default_unit(cls, unit):

        # Only kilometres and miles are allowed.
        if unit not in ("km", "mi"):
            raise ValueError("Default unit must be 'km' or 'mi'.")

        # Change the class variable.
        cls.default_unit = unit

    # This class method creates a Trail object from a dictionary.
    # This is useful when trail data comes from an API or JSON-like source.
    @classmethod
    def from_dict(cls, data):

        # Get the distance value from the dictionary.
        distance_value = data["distance"]

        # Get the unit from the dictionary.
        # If no unit is supplied, use the current platform default.
        distance_unit = data.get("unit", cls.default_unit)

        # Create a Distance object from the dictionary values.
        distance_object = Distance(distance_value, distance_unit)

        # Return a new Trail object.
        return cls(
            data["id"],
            data["name"],
            distance_object,
            data["elevation_gain_m"],
            data["difficulty"]
        )

    # This special method defines how two Trail objects are compared.
    # Two trails are considered equal if their ids are the same.
    def __eq__(self, other):

        # If the other value is not a Trail object,
        # Python should consider the comparison unsupported.
        if not isinstance(other, Trail):
            return NotImplemented

        # Compare the ids.
        return self.id == other.id

    # This optional method makes Trail objects easier to read when printed.
    def __str__(self):
        return (
            f"{self.name} - "
            f"{self.distance.magnitude} {self.distance.unit} - "
            f"{self.difficulty}"
        )