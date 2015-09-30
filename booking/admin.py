from django.contrib import admin

from .models import Delegate
from .forms import BookingForm


class DelegateAdmin(admin.ModelAdmin):
    list_display = ["ticket_number", "email"]
    form = BookingForm

    class Meta:
        model = Delegate


admin.site.register(Delegate, DelegateAdmin)
