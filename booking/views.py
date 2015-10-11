from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from .forms import BookingForm
from .models import Delegate


def booking(request):
    title = 'Make a Booking Now'
    form = BookingForm(request.POST or None)
    # None removes the default "field is required"
    
    if form.is_valid():
        form.save()
        # Saves the form to the database

        return HttpResponse(reverse())
        # Takes the delegate to a new page once complete.


    return render(request, 'booking.html', {'form': form})
    