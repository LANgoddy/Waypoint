# Import ABC and abstractmethod so Trail can become an abstract base class.
from abc import ABC, abstractmethod

# Import Distance because every trail still has a Distance object.
from distance import Distance


# This mixin provides elevation-related behaviour.
# A mixin is a small reusable class that adds one specific capability.
class ElevationMixin:

    # Calculate the grade percentage using elevation gain and trail distance.
    def grade_percent(self):

        # Convert trail distance to kilometres if necessary.
        distance_km = self.distance.convert("km").magnitude

        # Prevent division by zero.
        if distance_km == 0:
            return 0

        # Convert kilometres to metres.
        distance_m = distance_km * 1000

        # Calculate grade percentage.
        return (self.elevation_gain_m / distance_m) * 100


# This mixin provides rating-related behaviour.
class RatingMixin:

    # Set a rating value for the trail.
    def set_rating(self, rating):

        # Rating must be between 0 and 5.
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5.")

        self.rating = rating

    # Return the rating in a readable format.
    def rating_summary(self):

        # If no rating has been set yet, show a default message.
        if not hasattr(self, "rating"):
            return "No rating available"

        return f"{self.rating}/5 stars"


# Trail is now an abstract base class.
# It contains behaviour shared by all trail types.
class Trail(ABC):

    # Default distance unit used when a plain number is supplied.
    default_unit = "km"

    # Allowed difficulty values.
    ALLOWED_DIFFICULTIES = ("easy", "moderate", "hard", "expert")

    # The constructor stores information common to all trail types.
    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):

        # Store the trail id.
        self.id = trail_id

        # Store the trail name.
        self.name = name

        # If distance is already a Distance object, use it directly.
        if isinstance(distance, Distance):
            self.distance = distance

        # Otherwise, create a Distance using the current default unit.
        else:
            self.distance = Distance(distance, Trail.default_unit)

        # Validate elevation gain before storing it.
        if not Trail.is_valid_elevation(elevation_gain_m):
            raise ValueError("Elevation gain cannot be negative.")

        self.elevation_gain_m = elevation_gain_m

        # Store difficulty as internal data.
        self._difficulty = None

        # Validate and store difficulty.
        self.set_difficulty(difficulty)

    # Safely change the difficulty value.
    def set_difficulty(self, difficulty):

        if not Trail.is_valid_difficulty(difficulty):
            raise ValueError(
                "Difficulty must be easy, moderate, hard, or expert."
            )

        self._difficulty = difficulty

    # Read-only access to difficulty.
    @property
    def difficulty(self):
        return self._difficulty

    # Static validator for difficulty.
    @staticmethod
    def is_valid_difficulty(difficulty):
        return difficulty in Trail.ALLOWED_DIFFICULTIES

    # Static validator for elevation.
    @staticmethod
    def is_valid_elevation(elevation_gain_m):
        return elevation_gain_m >= 0

    # Class method for changing the default unit.
    @classmethod
    def set_default_unit(cls, unit):

        if unit not in ("km", "mi"):
            raise ValueError("Default unit must be 'km' or 'mi'.")

        cls.default_unit = unit

    # Alternate constructor for API-shaped dictionary data.
    @classmethod
    def from_dict(cls, data):

        distance_value = data["distance"]
        distance_unit = data.get("unit", cls.default_unit)

        distance_object = Distance(
            distance_value,
            distance_unit
        )

        return cls(
            data["id"],
            data["name"],
            distance_object,
            data["elevation_gain_m"],
            data["difficulty"]
        )

    # Two trails are equal when they have the same id.
    def __eq__(self, other):

        if not isinstance(other, Trail):
            return NotImplemented

        return self.id == other.id

    # Every concrete trail type MUST provide its own estimated time.
    @abstractmethod
    def estimated_time(self):
        pass

    # Every concrete trail type MUST provide its own summary.
    @abstractmethod
    def summary(self):
        pass


# DayHike inherits from Trail.
# It represents a trail intended to be completed in one day.
class DayHike(Trail):

    # Use super().__init__ to reuse Trail's constructor.
    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    # Day hikes use an average walking pace of 4 km per hour.
    def estimated_time(self):

        distance_km = self.distance.convert("km").magnitude

        hours = distance_km / 4

        return hours

    # Provide a summary specific to a day hike.
    def summary(self):

        return (
            f"Day Hike: {self.name} | "
            f"{self.distance.magnitude} {self.distance.unit} | "
            f"Difficulty: {self.difficulty}"
        )

    # Day hikes use a simple packing list.
    def packing_list(self):

        return [
            "Water",
            "Snacks",
            "Map",
            "First aid kit"
        ]


# GuidedDayHike is a second level of inheritance.
# It extends DayHike and adds guide information.
class GuidedDayHike(DayHike):

    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty,
        guide_name
    ):

        # Reuse DayHike's constructor.
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

        # Store the extra field added by GuidedDayHike.
        self.guide_name = guide_name

    # Extend the original summary rather than replacing it completely.
    def summary(self):

        # Call the parent DayHike summary first.
        original_summary = super().summary()

        # Add the guide information.
        return f"{original_summary} | Guide: {self.guide_name}"


# BackpackingRoute represents a longer multi-day route.
class BackpackingRoute(Trail):

    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):

        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    # Backpacking is slower because the hiker carries more gear.
    # We use an average pace of 3 km per hour.
    def estimated_time(self):

        distance_km = self.distance.convert("km").magnitude

        hours = distance_km / 3

        return hours

    # Provide a backpacking-specific summary.
    def summary(self):

        return (
            f"Backpacking Route: {self.name} | "
            f"{self.distance.magnitude} {self.distance.unit} | "
            f"Difficulty: {self.difficulty}"
        )

    # Override packing behaviour because backpacking needs more equipment.
    def packing_list(self):

        return [
            "Water",
            "Food",
            "Tent",
            "Sleeping bag",
            "Cooking equipment",
            "First aid kit"
        ]


# TrailRun represents a route intended for running.
class TrailRun(Trail):

    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):

        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    # Trail running is faster than hiking.
    # We use an average pace of 8 km per hour.
    def estimated_time(self):

        distance_km = self.distance.convert("km").magnitude

        hours = distance_km / 8

        return hours

    # Provide a running-specific summary.
    def summary(self):

        return (
            f"Trail Run: {self.name} | "
            f"{self.distance.magnitude} {self.distance.unit} | "
            f"Difficulty: {self.difficulty}"
        )


# This class combines two mixins with DayHike.
# It gains elevation tools, rating tools, and normal DayHike behaviour.
class RatedElevationDayHike(
    ElevationMixin,
    RatingMixin,
    DayHike
):
    pass