from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from .forms import BookingForm
from .models import Delegate


def booking(request):
    title = 'Make a Booking Now'
    form = BookingForm(request.POST)
    if form.is_valid():

        return HttpResponse('/thanks/')

    else:
        form = BookingForm()
        form = form.save()

    return render(request, 'booking/booking.html', {'form': form})
    