# Import the Distance class so total distance can be returned as a Distance object.
from distance import Distance


# This class represents a planned trip containing an ordered list of trails.
class Itinerary:

    # The __init__ method runs automatically when an Itinerary object is created.
    def __init__(self):

        # Create a new empty list for this specific itinerary.
        # Each Itinerary object gets its own independent list.
        self.trails = []

    # Add a Trail object to the end of the itinerary.
    def add_trail(self, trail):
        self.trails.append(trail)

    # Calculate the total distance of all trails in the itinerary.
    def total_distance(self):

        # If the itinerary has no trails,
        # return zero kilometres.
        if len(self.trails) == 0:
            return Distance(0, "km")

        # Use the unit of the first trail as the unit for the total.
        target_unit = self.trails[0].distance.unit

        # Start the running total at zero.
        total = 0

        # Go through each trail in order.
        for trail in self.trails:

            # Convert each trail distance into the target unit.
            converted_distance = trail.distance.convert(target_unit)

            # Add the converted magnitude to the running total.
            total += converted_distance.magnitude

        # Return the final total as a Distance object.
        return Distance(total, target_unit)