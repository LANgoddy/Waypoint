# Import Python's built-in logging module.
import logging

# Import render so Django can display HTML templates.
from django.shortcuts import render

# Import Django's generic class-based views.
from django.views.generic import ListView, DetailView

# Import the Trail model.
from .models import Trail

# Import the Trail search form.
from .forms import TrailSearchForm


# ---------------------------------------------------------
# LOGGER
# ---------------------------------------------------------

# Create a logger for this trails application.
logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# ABOUT VIEW
# ---------------------------------------------------------

# This view handles requests for the About page.
def about(request):

    # Record that the About page was requested.
    logger.info("About page requested.")

    # Render the About page HTML template.
    return render(request, "trails/about.html")


# ---------------------------------------------------------
# TRAIL LIST VIEW
# ---------------------------------------------------------

# This class displays Trail records from the database.
class TrailListView(ListView):

    # Tell Django which model this view uses.
    model = Trail

    # Tell Django which template should display the records.
    template_name = "trails/trail_list.html"

    # Give the trail list a clear variable name inside the template.
    context_object_name = "trails"

    # Show only two trails on each page.
    paginate_by = 2

    # Get and filter the Trail records displayed on the page.
    def get_queryset(self):

        # Record that the trail catalogue was requested.
        logger.info("Trail catalogue requested.")

        # Retrieve Trails and their related Parks efficiently.
        queryset = Trail.objects.select_related("park").all()

        # Get the text entered in the search box.
        query = self.request.GET.get("query")

        # If the user entered a search term, filter by trail name.
        if query:

            # Record the search term in the log.
            logger.info("Trail search performed for: %s", query)

            # Filter Trail records by name.
            queryset = queryset.filter(name__icontains=query)

        # Give the queryset a consistent order for pagination.
        queryset = queryset.order_by("name")

        # Return the final Trail records.
        return queryset

    # Add extra information that the template can use.
    def get_context_data(self, **kwargs):

        # Get the information Django already prepared.
        context = super().get_context_data(**kwargs)

        # Add the search form to the template.
        context["search_form"] = TrailSearchForm(self.request.GET)

        # Return everything to the template.
        return context


# ---------------------------------------------------------
# TRAIL DETAIL VIEW
# ---------------------------------------------------------

# This class displays one individual Trail record.
class TrailDetailView(DetailView):

    # Tell Django which model this view uses.
    model = Trail

    # Tell Django which template should display one trail.
    template_name = "trails/trail_detail.html"

    # Give the selected Trail object a clear name in the template.
    context_object_name = "trail"

    # Retrieve the Trail and its related Park efficiently.
    def get_queryset(self):

        # Record that a trail detail page was requested.
        logger.info("Trail detail page requested.")

        # Retrieve the Trail and Park in the same database query.
        return Trail.objects.select_related("park")