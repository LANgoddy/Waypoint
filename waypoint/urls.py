# Import Django's admin site.
from django.contrib import admin

# Import path so we can define URL routes.
from django.urls import path

# Import the views from the trails app.
from trails import views


# URL patterns tell Django which view to run for each web address.
urlpatterns = [

    # Django admin page.
    path("admin/", admin.site.urls),

    # About page.
    path("about/", views.about, name="about"),

    # Trail catalogue page.
    path("trails/", views.trail_list, name="trail_list"),
]