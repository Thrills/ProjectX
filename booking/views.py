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

        return HttpResponse('/thanks/'
        '<br>'
        '<a href="http://127.0.0.1:8000/booking/">Book Another Ticket</a>'
        '<br>'
        '<a href="">Register</a>'
        )
        # Takes the delegate to a new page once complete.

    #else:
    #    form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})
    