# Import path so we can define URL routes.
from django.urls import path

# Import the class-based views from this app.
from .views import TrailListView, TrailDetailView


# Give this app a URL namespace.
# This lets templates refer to URLs like trails:trail_list.
app_name = "trails"


# Define the URLs that belong to the trails app.
urlpatterns = [

    # Display the full trail catalogue.
    path(
        "",
        TrailListView.as_view(),
        name="trail_list"
    ),

    # Display one individual trail using its database primary key.
    path(
        "<int:pk>/",
        TrailDetailView.as_view(),
        name="trail_detail"
    ),
]