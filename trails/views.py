# Import render so Django can display HTML templates.
from django.shortcuts import render

# Import Django's generic class-based views.
from django.views.generic import ListView, DetailView

# Import the Trail model.
from .models import Trail

# Import the Trail search form.
from .forms import TrailSearchForm


# ---------------------------------------------------------
# ABOUT VIEW
# ---------------------------------------------------------

# This view handles requests for the About page.
def about(request):

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

    # Filter the Trail records based on the user's search.
    def get_queryset(self):

        # Start with all Trail records.
        queryset = Trail.objects.all()

        # Get the text entered in the search box.
        query = self.request.GET.get("query")

        # If the user entered a search term, filter by trail name.
        if query:
            queryset = queryset.filter(name__icontains=query)

        # Return the final list of Trail records.
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