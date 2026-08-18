# Import Django's admin site.
from django.contrib import admin

# Import path and include for URL routing.
from django.urls import path, include

# Import the About view from the MAIN trails app.
from trails.views import about


# ---------------------------------------------------------
# MAIN PROJECT URLS
# ---------------------------------------------------------

urlpatterns = [

    # Django admin page.
    path("admin/", admin.site.urls),

    # About page.
    path("about/", about, name="about"),

    # Send all /trails/ URLs to the MAIN trails app urls.py file.
    path(
        "trails/",
        include("trails.urls")
    ),
]