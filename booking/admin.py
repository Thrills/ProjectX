from django.contrib import admin

from .models import Delegate
#class DelegateAdmin(admin.ModelAdmin):
    #fields = ['delegate_ticketNumber', 'delegate_name', 'delegate_surname', 'delegate_dietaryRequirements']
admin.site.register(Delegate)#, DelegateAdmin)

from .models import Ticket
#class TicketAdmin(admin.Ticket):
    #fields = ['TicketNumber']
admin.site.register(Ticket)#, TicketAdmin)


