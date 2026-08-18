# Import render so Django can display HTML templates.
from django.shortcuts import render


# This view handles requests for the About page.
def about(request):

    # Render the About page HTML template.
    return render(request, "trails/about.html")


# This view handles requests for the trail catalogue page.
def trail_list(request):

    # Render the Trail Catalogue HTML template.
    return render(request, "trails/trail_list.html")