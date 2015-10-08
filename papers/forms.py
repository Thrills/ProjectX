from django import forms

from .models import RegisteredUser, Paper, Review

class RegisteredUserForm(forms.ModelForm):
	class Meta:
		model = RegisteredUser
		fields = ['name', 'surname', 'institution','role', 'country', 'email']

class PaperForm(forms.ModelForm):
	class Meta:
		model = Paper
		fields = ['title', 'abstract', 'language','paper_file'] # 'paper_avgScore', 'paper_accepted']
		# paper_file = forms.FileField(
  #       	label='Select a file'
  #   	 )

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['review_score', 'comments']

