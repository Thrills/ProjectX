from django import forms

from .models import RegisteredUser, Paper, Review

class RegisteredUserForm(forms.ModelForm):
	class Meta:
		model = RegisteredUser
		fields = ['name', 'surname', 'institution','role', 'country', 'email']

class PaperForm(forms.ModelForm):
	class Meta:
		model = Paper
		fields = ['abstract', 'language', 'paper_avgScore', 'paper_accepted']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['review_score', 'review_score']

