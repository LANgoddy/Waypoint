# Import Django's testing tools.
from django.test import TestCase

# Import reverse so tests can use named URLs.
from django.urls import reverse

# Import the Park and Trail database models.
from .models import Park, Trail


# ---------------------------------------------------------
# TRAIL MODEL TESTS
# ---------------------------------------------------------

# Test the Trail and Park database models.
class TrailModelTests(TestCase):

    # This method runs before each individual test.
    def setUp(self):

        # Create a Park for the test database.
        self.park = Park.objects.create(
            name="Rouge National Urban Park",
            description="Test park for Waypoint."
        )

        # Create one Trail connected to the Park.
        self.trail = Trail.objects.create(
            park=self.park,
            name="Vista Trail",
            distance_km=7.5,
            difficulty="moderate",
            elevation_gain_m=180
        )

    # Test that a Park displays its name correctly.
    def test_park_string_representation(self):

        self.assertEqual(
            str(self.park),
            "Rouge National Urban Park"
        )

    # Test that a Trail displays its name correctly.
    def test_trail_string_representation(self):

        self.assertEqual(
            str(self.trail),
            "Vista Trail"
        )


# ---------------------------------------------------------
# TRAIL LIST VIEW TESTS
# ---------------------------------------------------------

# Test the trail catalogue page.
class TrailListViewTests(TestCase):

    # Create test data before each test.
    def setUp(self):

        self.park = Park.objects.create(
            name="Rouge National Urban Park",
            description="Test park for Waypoint."
        )

        # Create three trails for testing.
        Trail.objects.create(
            park=self.park,
            name="Vista Trail",
            distance_km=7.5,
            difficulty="moderate",
            elevation_gain_m=180
        )

        Trail.objects.create(
            park=self.park,
            name="Cedar Ridge Trail",
            distance_km=4.2,
            difficulty="easy",
            elevation_gain_m=90
        )

        Trail.objects.create(
            park=self.park,
            name="Mast Trail",
            distance_km=11.0,
            difficulty="hard",
            elevation_gain_m=320
        )

    # Test that the trail catalogue loads successfully.
    def test_trail_list_page_returns_success(self):

        response = self.client.get(
            reverse("trails:trail_list")
        )

        self.assertEqual(
            response.status_code,
            200
        )

    # Test that a trail from page one appears.
    def test_trail_list_displays_trail(self):

        response = self.client.get(
            reverse("trails:trail_list")
        )

        # Cedar Ridge Trail appears on page one
        # because the queryset is ordered alphabetically.
        self.assertContains(
            response,
            "Cedar Ridge Trail"
        )

    # Test that searching by trail name works.
    def test_trail_search(self):

        response = self.client.get(
            reverse("trails:trail_list"),
            {"query": "Vista"}
        )

        # Vista Trail should appear in the search results.
        self.assertContains(
            response,
            "Vista Trail"
        )

        # Mast Trail should not appear.
        self.assertNotContains(
            response,
            "Mast Trail"
        )

    # Test that pagination limits page one to two trails.
    def test_trail_pagination(self):

        response = self.client.get(
            reverse("trails:trail_list")
        )

        # Confirm pagination is active.
        self.assertTrue(
            response.context["is_paginated"]
        )

        # Confirm only two trails appear on page one.
        self.assertEqual(
            len(response.context["trails"]),
            2
        )


# ---------------------------------------------------------
# TRAIL DETAIL VIEW TESTS
# ---------------------------------------------------------

# Test the individual trail detail page.
class TrailDetailViewTests(TestCase):

    # Create test data before each test.
    def setUp(self):

        self.park = Park.objects.create(
            name="Rouge National Urban Park",
            description="Test park for Waypoint."
        )

        self.trail = Trail.objects.create(
            park=self.park,
            name="Vista Trail",
            distance_km=7.5,
            difficulty="moderate",
            elevation_gain_m=180
        )

    # Test that the trail detail page loads successfully.
    def test_trail_detail_page_returns_success(self):

        response = self.client.get(
            reverse(
                "trails:trail_detail",
                args=[self.trail.pk]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

    # Test that the detail page displays the correct trail.
    def test_trail_detail_displays_correct_trail(self):

        response = self.client.get(
            reverse(
                "trails:trail_detail",
                args=[self.trail.pk]
            )
        )

        self.assertContains(
            response,
            "Vista Trail"
        )

        self.assertContains(
            response,
            "7.5"
        )

        self.assertContains(
            response,
            "180"
        )