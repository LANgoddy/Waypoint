# Import all Week 8 classes.
from distance import Distance
from trail import (
    Trail,
    DayHike,
    GuidedDayHike,
    BackpackingRoute,
    TrailRun,
    RatedElevationDayHike
)


# ---------------------------------------------------------
# TEST 1: DISTANCE ADDITION
# ---------------------------------------------------------

distance1 = Distance(3, "km")
distance2 = Distance(2, "km")

total_distance = distance1 + distance2

print("TEST 1 - Distance addition:")
print(total_distance)


# ---------------------------------------------------------
# TEST 2: DISTANCE SUBTRACTION
# ---------------------------------------------------------

distance3 = Distance(10, "km")
distance4 = Distance(4, "km")

remaining_distance = distance3 - distance4

print("\nTEST 2 - Distance subtraction:")
print(remaining_distance)


# ---------------------------------------------------------
# TEST 3: DISTANCE EQUALITY
# ---------------------------------------------------------

distance5 = Distance(5, "km")
distance6 = Distance(5, "km")

print("\nTEST 3 - Distance equality:")
print(distance5 == distance6)


# ---------------------------------------------------------
# TEST 4: DISTANCE SORTING
# ---------------------------------------------------------

distances = [
    Distance(8, "km"),
    Distance(2, "km"),
    Distance(5, "km"),
    Distance(1, "km")
]

# sorted() uses the __lt__ method from Distance.
sorted_distances = sorted(distances)

print("\nTEST 4 - Sorted distances:")

for distance in sorted_distances:
    print(distance)


# ---------------------------------------------------------
# TEST 5: MIXED UNITS
# ---------------------------------------------------------

# Mixed units are automatically converted.
mixed_total = Distance(3, "km") + Distance(2, "mi")

print("\nTEST 5 - Mixed-unit addition:")
print(mixed_total)


# ---------------------------------------------------------
# TEST 6: CREATE DIFFERENT TRAIL TYPES
# ---------------------------------------------------------

day_hike = DayHike(
    1,
    "Maple Ridge Trail",
    Distance(8, "km"),
    300,
    "moderate"
)

backpacking_route = BackpackingRoute(
    2,
    "Mountain Pass Route",
    Distance(18, "km"),
    900,
    "hard"
)

trail_run = TrailRun(
    3,
    "River Run Trail",
    Distance(12, "km"),
    200,
    "moderate"
)

guided_hike = GuidedDayHike(
    4,
    "Forest Discovery Trail",
    Distance(6, "km"),
    150,
    "easy",
    "Alex"
)

print("\nTEST 6 - Trail summaries:")
print(day_hike.summary())
print(backpacking_route.summary())
print(trail_run.summary())
print(guided_hike.summary())


# ---------------------------------------------------------
# TEST 7: POLYMORPHISM
# ---------------------------------------------------------

# Each object responds to estimated_time()
# using the version defined in its own class.
trail_list = [
    day_hike,
    backpacking_route,
    trail_run,
    guided_hike
]

print("\nTEST 7 - Polymorphic estimated times:")

for trail in trail_list:
    print(
        trail.name,
        "-",
        trail.estimated_time(),
        "hours"
    )


# ---------------------------------------------------------
# TEST 8: ABSTRACT CLASS
# ---------------------------------------------------------

# Trail is abstract and should not be created directly.
try:
    invalid_trail = Trail(
        5,
        "Generic Trail",
        Distance(5, "km"),
        100,
        "easy"
    )

except TypeError as error:
    print("\nTEST 8 - Abstract Trail rejected:")
    print(error)


# ---------------------------------------------------------
# TEST 9: PACKING-LIST OVERRIDE
# ---------------------------------------------------------

print("\nTEST 9 - Day hike packing list:")
print(day_hike.packing_list())

print("Backpacking packing list:")
print(backpacking_route.packing_list())


# ---------------------------------------------------------
# TEST 10: MIXINS
# ---------------------------------------------------------

rated_hike = RatedElevationDayHike(
    6,
    "Cliff View Trail",
    Distance(5, "km"),
    500,
    "hard"
)

# Rating behaviour comes from RatingMixin.
rated_hike.set_rating(4.5)

print("\nTEST 10 - Mixin behaviour:")
print("Grade:", rated_hike.grade_percent(), "%")
print("Rating:", rated_hike.rating_summary())


# ---------------------------------------------------------
# TEST 11: METHOD RESOLUTION ORDER
# ---------------------------------------------------------

print("\nTEST 11 - MRO:")

for class_type in RatedElevationDayHike.__mro__:
    print(class_type.__name__)


# ---------------------------------------------------------
# TEST 12: DUCK TYPING
# ---------------------------------------------------------

# FakeTrail does not inherit from Trail.
# It simply provides the method needed by the loop.
class FakeTrail:

    def __init__(self, name):
        self.name = name

    def estimated_time(self):
        return 1.25


fake_trail = FakeTrail("Testing Trail")

mixed_trails = [
    day_hike,
    backpacking_route,
    trail_run,
    fake_trail
]

print("\nTEST 12 - Duck typing:")

for trail in mixed_trails:
    print(
        trail.name,
        "-",
        trail.estimated_time(),
        "hours"
    )