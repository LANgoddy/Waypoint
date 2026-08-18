# Import Django's admin site.
from django.contrib import admin

# Import include so the main project can use URLs from the trails app.
from django.urls import path, include

# Import render so we can keep a simple About page.
from django.shortcuts import render


# ---------------------------------------------------------
# ABOUT VIEW
# ---------------------------------------------------------

# This simple function keeps the About page working.
def about(request):
    return render(request, "trails/about.html")


# ---------------------------------------------------------
# MAIN PROJECT URLS
# ---------------------------------------------------------

urlpatterns = [

    # Django administration page.
    path("admin/", admin.site.urls),

    # About page.
    path("about/", about, name="about"),

    # Send all /trails/ URLs to trails/urls.py.
    path(
        "trails/",
        include("trails.urls")
    ),
]