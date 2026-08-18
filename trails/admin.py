# Import Django's admin tools.
from django.contrib import admin

# Import the Park and Trail models from this app.
from .models import Park, Trail


# ---------------------------------------------------------
# PARK ADMIN
# ---------------------------------------------------------

# Customize how Park records appear in Django Admin.
@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):

    # Show these columns on the Park list page.
    list_display = (
        "id",
        "name",
    )

    # Allow searching parks by name.
    search_fields = (
        "name",
    )


# ---------------------------------------------------------
# TRAIL ADMIN
# ---------------------------------------------------------

# Customize how Trail records appear in Django Admin.
@admin.register(Trail)
class TrailAdmin(admin.ModelAdmin):

    # Show these columns on the Trail list page.
    list_display = (
        "id",
        "name",
        "park",
        "distance_km",
        "difficulty",
        "elevation_gain_m",
    )

    # Add filters on the right side of Django Admin.
    list_filter = (
        "difficulty",
        "park",
    )

    # Allow searching trails by name.
    search_fields = (
        "name",
    )

    # Default ordering for the Trail list.
    ordering = (
        "name",
    )