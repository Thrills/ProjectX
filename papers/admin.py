from django.contrib import admin

from .forms import RegisteredUserForm, PaperForm, ReviewForm

from .models import RegisteredUser, Paper, Review

class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "surname", "role", "institution", "email"]
    form = RegisteredUserForm                                    # Creates fieldsets for the data about  users
    class Meta:
        model = RegisteredUser
        ordering = ('pk')

admin.site.register(RegisteredUser, RegisteredUserAdmin)

class PaperAdmin(admin.ModelAdmin):
    list_display = ["__str__", "paper_submissionDate", "paper_avgScore", "paper_accepted"]         # Different data the Admin will be able to view
    form = PaperForm
    #class Meta:
     #   model = Paper

admin.site.register(Paper, PaperAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id", "review_score"]
    form = ReviewForm
    #class Meta:
    #    model = Review

admin.site.register(Review, ReviewAdmin)


