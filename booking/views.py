from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import BookingForm
from .models import Delegate


def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
    # None removes the default "field is required"
        if form.is_valid():
            form.save()
        # Saves the form to the database

            return HttpResponseRedirect(reverse('success'))
        # Takes the delegate to a new page once complete.
        else:
            form = ReviewForm()
        return render(request, 'booking.html', {'form': form})

    return render(request, 'booking.html', {'form': form})
    
 