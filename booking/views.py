from django.shortcuts import get_object_or_404, render

from .models import Delegate


def booking(request, delegate_email):
    question = get_object_or_404(Delegate, pk=delegate_email)
    return render(request, 'booking/booking.html', {'question': question})