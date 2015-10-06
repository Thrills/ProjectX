from django import forms

from .models import CommitteeMember, Paper, Reviewer, Review, Author

class CommitteeMemberForm(forms.ModelForm):
	class Meta:
		model = CommitteeMember
		fields = ['cm_id', 'cm_name', 'cm_surname', 'institution', 'email']

class PaperForm(forms.ModelForm):
	class Meta:
		model = Paper
		fields = ['abstract', 'language', 'paper_avgScore', 'paper_accepted']

class ReviewerForm(forms.ModelForm):
	class Meta:
		model = Reviewer
		fields = ['reviewer_name', 'reviewer_surname', 'institution', 'email']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['review_score', 'review_score']

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ['author_name', 'author_surname', 'institution', 'country', 'email']