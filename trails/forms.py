# Import Django's form tools.
from django import forms


# ---------------------------------------------------------
# TRAIL SEARCH FORM
# ---------------------------------------------------------

# This form lets users search for trails by name.
class TrailSearchForm(forms.Form):

    # A simple text box for entering a search term.
    query = forms.CharField(
        required=False,
        label="Search Trails",
        max_length=100
    )