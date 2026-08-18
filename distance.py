# This class represents a distance value used by the Waypoint application.
# A Distance object stores a magnitude and a unit, such as 5 km or 10 mi.
class Distance:

    # The __init__ method runs automatically whenever a Distance object is created.
    def __init__(self, magnitude, unit):

        # Distance cannot be negative.
        if magnitude < 0:
            raise ValueError("Distance cannot be negative.")

        # Only kilometres and miles are supported.
        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'.")

        # Store the validated values as internal object data.
        self._magnitude = magnitude
        self._unit = unit

    # Read-only access to magnitude.
    @property
    def magnitude(self):
        return self._magnitude

    # Read-only access to unit.
    @property
    def unit(self):
        return self._unit

    # Convert the distance into another supported unit.
    def convert(self, target_unit):

        if target_unit not in ("km", "mi"):
            raise ValueError("Target unit must be 'km' or 'mi'.")

        # If the target unit is already the same,
        # return a new Distance object with the same value.
        if target_unit == self._unit:
            return Distance(self._magnitude, self._unit)

        # Convert kilometres to miles.
        if self._unit == "km" and target_unit == "mi":
            converted_magnitude = self._magnitude * 0.621371
            return Distance(converted_magnitude, "mi")

        # Convert miles to kilometres.
        if self._unit == "mi" and target_unit == "km":
            converted_magnitude = self._magnitude * 1.60934
            return Distance(converted_magnitude, "km")

    # Add two Distance objects together.
    # Mixed units are automatically converted to the unit of the left object.
    def __add__(self, other):

        # Only another Distance object can be added.
        if not isinstance(other, Distance):
            return NotImplemented

        # Convert the other distance into this object's unit.
        other_converted = other.convert(self._unit)

        # Add the magnitudes.
        total = self._magnitude + other_converted.magnitude

        # Return a new Distance object.
        return Distance(total, self._unit)

    # Subtract one Distance object from another.
    def __sub__(self, other):

        # Only another Distance object can be subtracted.
        if not isinstance(other, Distance):
            return NotImplemented

        # Convert the other distance into this object's unit.
        other_converted = other.convert(self._unit)

        # Calculate the new magnitude.
        result = self._magnitude - other_converted.magnitude

        # Distance objects are not allowed to be negative.
        if result < 0:
            raise ValueError("Distance subtraction cannot produce a negative value.")

        # Return the result as a new Distance object.
        return Distance(result, self._unit)

    # Compare two Distance objects for equality.
    def __eq__(self, other):

        if not isinstance(other, Distance):
            return NotImplemented

        # Convert the other distance into this object's unit.
        other_converted = other.convert(self._unit)

        # Use a small tolerance because floating-point conversions
        # may not produce exactly identical decimal values.
        return abs(self._magnitude - other_converted.magnitude) < 0.0001

    # Support the less-than operator.
    def __lt__(self, other):

        if not isinstance(other, Distance):
            return NotImplemented

        # Convert before comparing.
        other_converted = other.convert(self._unit)

        return self._magnitude < other_converted.magnitude

    # Support the greater-than operator.
    def __gt__(self, other):

        if not isinstance(other, Distance):
            return NotImplemented

        # Convert before comparing.
        other_converted = other.convert(self._unit)

        return self._magnitude > other_converted.magnitude

    # Provide a friendly readable version of the object.
    def __str__(self):
        return f"{self._magnitude} {self._unit}"

    # Provide a developer-friendly representation of the object.
    def __repr__(self):
        return f"Distance({self._magnitude!r}, {self._unit!r})"