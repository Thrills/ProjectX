from django.contrib import admin

from .models import Chairperson
admin.site.register(Chairperson)

from .models import CommitteeMember
#class CommitteeMemberAdmin(admin.ModelAdmin):
    #field = ['cm_name', 'cm_surname', 'cm_institutions', 'cm_email']
admin.site.register(CommitteeMember, #CommitteeMemberAdmin)

from .models import Paper
#class PaperAdmin(admin.ModelAdmin):
    #fields = ['paper_code', 'paper_submissionDate', 'paper_submissionUpdate ', 'paper_avgScore', 'paper_accepted']
admin.site.register(Paper, #PaperAdmin)

from .models import Reviewer
#class ReviewerAdmin(admin.ModelAdmin):
    #field = ['reviewer_id', 'reviewer_name', 'reviewer_surname', 'reviewer_institution', 'reviewer_email']
admin.site.register(Reviewer, #ReviewerAdmin)

from .models import Review
admin.site.register(Review)

from .models import Author
admin.site.register(Author)
