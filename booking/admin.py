from django.contrib import admin

from .models import Delegate
from .forms import BookingForm

# Creates the admin database at the backend for bookingform 
class DelegateAdmin(admin.ModelAdmin):
    list_display = ["__str__", "delegate_name", "delegate_surname", "email"]
    form = BookingForm
    # inherits attributes from the model

admin.site.register(Delegate, DelegateAdmin)
