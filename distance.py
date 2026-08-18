# This class represents a distance value used by the Waypoint application.
# A Distance object stores a magnitude and a unit, such as 5 km or 10 mi.
class Distance:

    # The __init__ method runs automatically whenever a new Distance object is created.
    # magnitude represents the numerical distance.
    # unit represents the measurement unit and must be either "km" or "mi".
    def __init__(self, magnitude, unit):

        # A distance cannot be negative.
        # If a negative number is supplied, stop the program and raise a ValueError.
        if magnitude < 0:
            raise ValueError("Distance cannot be negative.")

        # Waypoint only supports kilometres and miles.
        # Any other measurement unit is rejected.
        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'.")

        # Store the validated magnitude as internal object data.
        self._magnitude = magnitude

        # Store the validated unit as internal object data.
        self._unit = unit

    # Provide read-only access to the magnitude.
    # This allows us to use distance.magnitude instead of distance._magnitude.
    @property
    def magnitude(self):
        return self._magnitude

    # Provide read-only access to the unit.
    # This allows us to use distance.unit instead of distance._unit.
    @property
    def unit(self):
        return self._unit

    # Convert the distance between kilometres and miles.
    # The method returns a NEW Distance object rather than changing the original object.
    def convert(self, target_unit):

        # Check that the requested target unit is valid.
        if target_unit not in ("km", "mi"):
            raise ValueError("Target unit must be 'km' or 'mi'.")

        # If the requested unit is already the current unit,
        # return a new Distance object containing the same values.
        if target_unit == self._unit:
            return Distance(self._magnitude, self._unit)

        # Convert kilometres to miles.
        # 1 kilometre is approximately 0.621371 miles.
        if self._unit == "km" and target_unit == "mi":
            converted_magnitude = self._magnitude * 0.621371
            return Distance(converted_magnitude, "mi")

        # Convert miles to kilometres.
        # 1 mile is approximately 1.60934 kilometres.
        if self._unit == "mi" and target_unit == "km":
            converted_magnitude = self._magnitude * 1.60934
            return Distance(converted_magnitude, "km")