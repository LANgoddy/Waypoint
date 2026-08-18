# Import path so we can define URL routes.
from django.urls import path

# Import the class-based views from the MAIN trails app.
from .views import TrailListView, TrailDetailView


# Give the MAIN trails app its own URL namespace.
app_name = "trails"


# Define the URLs that belong to the MAIN trails app.
urlpatterns = [

    # Show the full trail catalogue.
    path(
        "",
        TrailListView.as_view(),
        name="trail_list"
    ),

    # Show one individual trail using its database ID.
    path(
        "<int:pk>/",
        TrailDetailView.as_view(),
        name="trail_detail"
    ),
]