# Import Django's generic class-based views.
from django.views.generic import ListView, DetailView

# Import the Trail model from this app.
from .models import Trail


# ---------------------------------------------------------
# TRAIL LIST VIEW
# ---------------------------------------------------------

# This class displays all Trail records from the database.
class TrailListView(ListView):

    # Tell Django which model this view uses.
    model = Trail

    # Tell Django which template should display the records.
    template_name = "trails/trail_list.html"

    # Give the trail list a clear variable name inside the template.
    context_object_name = "trails"


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