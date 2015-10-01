from django.contrib import admin

from .models import Delegate
from .forms import BookingForm


class DelegateAdmin(admin.ModelAdmin):
    list_display = ["email"]
    form = BookingForm

admin.site.register(Delegate, DelegateAdmin)
