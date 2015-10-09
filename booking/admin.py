from django.contrib import admin

from .models import Delegate
from .forms import BookingForm


class DelegateAdmin(admin.ModelAdmin):
    list_display = ["__str__", "delegate_name", "delegate_surname", "email"]
    form = BookingForm

admin.site.register(Delegate, DelegateAdmin)
