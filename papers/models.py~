import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Chairperson(models.Model):
    cp_username = models.CharField(max_length=30)
    cp_password = models.CharField(max_length=30)
    def __str__(self):
    	return self.chairperson_text

class CommitteeMember(models.Model):
    cm_name = models.CharField(max_length=30)
    cm_surname = models.CharField(max_length=30, primary_key=True)
    cm_institution = models.CharField(max_length=50)
    cm_email = models.EmailField(max_length=50)
    def __str__(self):
    	return self.committeemember_text

class Paper(models.Model):
    paper_authorNames = models.CharField(max_length=100)
    author_id = models.ForeignKey('Author')
    paper_submissionDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    paper_submissionUpdate = models.DateTimeField(auto_now=True, auto_now_add=False)
    paper_abstract = models.CharField(max_length=300)
    paper_language = models.CharField(max_length=20)
    paper_code = models.CharField(max_length=10, primary_key=True)
    paper_reviewCode = models.CharField(max_length=10)
    paper_avgScore = models.CharField(max_length=2, blank=True, null=True)
    paper_accepted = models.NullBooleanField()
    def __str__(self):
    	return self.paper_text
    

class Reviewer(models.Model):
    reviewer_name = models.CharField(max_length=30)
    reviewer_surname = models.CharField(max_length=30)
    reviewer_id = models.CharField(max_length=10, primary_key=True)
    reviewer_institution = models.CharField(max_length=50)
    reviewer_email = models.EmailField(max_length=50)
    reviewer_paperCode = models.CharField(max_length=10)
    reviewer_reviewCode = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
    	return self.reviewer_text

class Review(models.Model):
    review_score = models.CharField(max_length=2)
    review_reviewCode = models.CharField(max_length=10, primary_key=True)
    reviewer_id = models.ForeignKey('Reviewer')
    review_paperCode = models.CharField(max_length=10)
    def __str__(self):
    	return self.review_text
    
class Author(models.Model):
    author_name = models.CharField(max_length=30)
    author_surname = models.CharField(max_length=30)
    author_id = models.CharField(max_length=10, primary_key=True)
    author_institution = models.CharField(max_length=50)
    author_country = models.CharField(max_length=50, blank=True)
    author_email = models.EmailField(max_length=50)
    def __str__(self):
    	return self.author_text
