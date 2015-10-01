from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import BookingForm
from .models import Delegate


def booking(request):
    title = 'Make a Booking Now'
    form = BookingForm(request.POST)
    if form.is_valid():
        # #print request.POST['email'] unsure !!
        form.save()
        form.process()
    

"""    instance = form.save(commit=False)

    delegate_name = form.cleaned_data.get("delegate_name")
    if not delegate_name:
        delegate_name = "New full name"
    instance.delegate_name = delegate_name
    # if not instance.delegate_name:
    # instance.delegate_name = "Marco"
    instance.save()
    context = {
        "title": "Thank you"
    }

    if request.user.is_authenticated() and request.user.is_staff:
         print(Delegate.objects.all())
    i = 1
    for instance in Delegate.objects.all():
    print(i)
    print(instance.delegate_name)
    i += 1 

        queryset = Delegate.objects.all().order_by('-timestamp')  # .filter(delegate_name__iexact="Marco")
    # print(Delegate.objects.all().order_by('-timestamp').filter(delegate_name__iexact="Marco").count())
    context = {
        "queryset": queryset
    }
    return render(request, "booking/booking.html", context) """
