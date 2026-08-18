# Import all Week 7 classes.
from distance import Distance
from trail import Trail
from itinerary import Itinerary


# ---------------------------------------------------------
# TEST 1: DISTANCE
# ---------------------------------------------------------

# Create a valid distance.
distance1 = Distance(5, "km")

print("TEST 1 - Distance:")
print(distance1.magnitude, distance1.unit)

# Convert kilometres to miles.
distance_in_miles = distance1.convert("mi")

print("Converted to miles:")
print(distance_in_miles.magnitude, distance_in_miles.unit)

# Convert the miles back to kilometres.
distance_back_to_km = distance_in_miles.convert("km")

print("Converted back to kilometres:")
print(distance_back_to_km.magnitude, distance_back_to_km.unit)


# ---------------------------------------------------------
# TEST 2: TRAIL CREATED NORMALLY
# ---------------------------------------------------------

trail1 = Trail(
    1,
    "Maple Ridge Trail",
    Distance(5, "km"),
    250,
    "moderate"
)

print("\nTEST 2 - Trail:")
print(trail1)


# ---------------------------------------------------------
# TEST 3: TRAIL CREATED FROM A DICTIONARY
# ---------------------------------------------------------

trail_data = {
    "id": 2,
    "name": "Pine Valley Trail",
    "distance": 8,
    "unit": "km",
    "elevation_gain_m": 400,
    "difficulty": "hard"
}

trail2 = Trail.from_dict(trail_data)

print("\nTEST 3 - Trail from dictionary:")
print(trail2)


# ---------------------------------------------------------
# TEST 4: TRAIL EQUALITY
# ---------------------------------------------------------

# This trail has different information,
# but it uses the same id as trail1.
duplicate_trail = Trail(
    1,
    "Different Trail Name",
    Distance(20, "km"),
    900,
    "expert"
)

print("\nTEST 4 - Same id means trails are equal:")
print(trail1 == duplicate_trail)


# ---------------------------------------------------------
# TEST 5: DEFAULT UNIT
# ---------------------------------------------------------

# Create a trail before changing the default unit.
before_change = Trail(
    3,
    "Before Default Change",
    4,
    100,
    "easy"
)

print("\nTEST 5 - Before changing default unit:")
print(before_change.distance.magnitude, before_change.distance.unit)

# Change the class default unit to miles.
Trail.set_default_unit("mi")

# Create a new trail after the default was changed.
after_change = Trail(
    4,
    "After Default Change",
    4,
    100,
    "easy"
)

print("After changing default unit:")
print(after_change.distance.magnitude, after_change.distance.unit)

# Show that the old trail kept its original unit.
print("Old trail still has:")
print(before_change.distance.magnitude, before_change.distance.unit)


# ---------------------------------------------------------
# TEST 6: ITINERARY
# ---------------------------------------------------------

trail3 = Trail(
    5,
    "Lake View Trail",
    Distance(3, "km"),
    150,
    "easy"
)

itinerary1 = Itinerary()

itinerary1.add_trail(trail1)
itinerary1.add_trail(trail2)
itinerary1.add_trail(trail3)

total = itinerary1.total_distance()

print("\nTEST 6 - Itinerary total:")
print(total.magnitude, total.unit)


# ---------------------------------------------------------
# TEST 7: ITINERARIES HAVE SEPARATE LISTS
# ---------------------------------------------------------

itinerary2 = Itinerary()

print("\nTEST 7 - Separate itinerary lists:")
print("Itinerary 1 number of trails:", len(itinerary1.trails))
print("Itinerary 2 number of trails:", len(itinerary2.trails))


# ---------------------------------------------------------
# TEST 8: INVALID DIFFICULTY
# ---------------------------------------------------------

# Try to create a trail with an invalid difficulty.
# The Trail class should reject it by raising a ValueError.
try:
    invalid_trail = Trail(
        6,
        "Invalid Trail",
        Distance(5, "km"),
        200,
        "impossible"
    )

# Catch the expected ValueError so the rest of the program does not crash.
except ValueError as error:
    print("\nTEST 8 - Invalid difficulty rejected:")
    print(error)


# ---------------------------------------------------------
# TEST 9: NEGATIVE DISTANCE
# ---------------------------------------------------------

# Try to create an invalid negative distance.
# The Distance class should reject it by raising a ValueError.
try:
    invalid_distance = Distance(-5, "km")

# Catch the expected ValueError and display the validation message.
except ValueError as error:
    print("\nTEST 9 - Negative distance rejected:")
    print(error)