from django.contrib import admin

from .models import CommitteeMember, Paper, Reviewer, Review, Author

class CommitteeMemberAdmin(admin.ModelAdmin):
    fieldsets = [                                                      # Creates fieldsets for the data about CM members
	('Personal Information', {'fields': ['cm_id', 'cm_name', 'cm_surname', 'cm_institution', 'cm_email']}),
]

admin.site.register(CommitteeMember, CommitteeMemberAdmin)

class PaperAdmin(admin.ModelAdmin):
    fieldsets = [
	('Paper Details', {'fields': ['paper_code', 'paper_submissionDate', 'paper_avgScore', 'paper_accepted']}) # Different data the Admin will be able to view
]

admin.site.register(Paper, PaperAdmin)

class ReviewerAdmin(admin.ModelAdmin):
    fieldsets = [
	('Personal Information', {'fields': ['reviewer_id', 'reviewer_name', 'reviewer_surname', 'reviewer_institution', 'reviewer_email']})
]

admin.site.register(Reviewer, ReviewerAdmin)

class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
	('Review Details', {'fields': ['reviewer_id', 'review_score', 'paper_code']})
]

admin.site.register(Review, ReviewAdmin)

class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
	('Personal Information',
     {'fields': ['author_id', 'author_name', 'author_surname', 'author_institution', 'author_email']})
]

admin.site.register(Author, AuthorAdmin)
