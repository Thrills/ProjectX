from django.contrib import admin

from .forms import CommitteeMemberForm, PaperForm, ReviewerForm, ReviewForm, AuthorForm

from .models import CommitteeMember, Paper, Reviewer, Review, Author

class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ["__str__", "cm_id", "institution", "email"]
    form = CommitteeMemberForm                                    # Creates fieldsets for the data about CM members
    #class Meta:
    #    model = CommitteeMember

admin.site.register(CommitteeMember, CommitteeMemberAdmin)

class PaperAdmin(admin.ModelAdmin):
    list_display = ["__str__", "paper_submissionDate", "paper_avgScore", "paper_accepted"]         # Different data the Admin will be able to view
    form = PaperForm
    #class Meta:
     #   model = Paper

admin.site.register(Paper, PaperAdmin)

class ReviewerAdmin(admin.ModelAdmin):
    list_display = ["__str__", "reviewer_id", "institution", "email"]
    form = ReviewerForm
    #class Meta:
    #    model = Reviewer

admin.site.register(Reviewer, ReviewerAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["__str__", "reviewer_id", "review_score"]
    form = ReviewForm
    #class Meta:
    #    model = Review

admin.site.register(Review, ReviewAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author_id", "institution", "email"]
    form = AuthorForm
    #class Meta:
    #    models = Author

admin.site.register(Author, AuthorAdmin)
