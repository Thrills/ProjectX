import datetime

from django.db import models
# from django.utils import timezone

# Create your models here.

class Chairperson(models.Model):
    cp_username = models.CharField(max_length=30)
    cp_password = models.CharField(max_length=30)

class CommitteeMember(models.Model):
    cm_id = models.CharField(max_length=3, primary_key=True)
    cm_name = models.CharField(max_length=30)
    cm_surname = models.CharField(max_length=30,)
    cm_institution = models.CharField(max_length=50)
    cm_email = models.EmailField(max_length=50)
    def __str__(self):
    	return '%s %s %s' % (self.cm_id, self.cm_name, self.cm_surname)

class Paper(models.Model):
    author_id = models.ForeignKey('Author')
    paper_submissionDate = models.DateTimeField(auto_now=False)
    paper_abstract = models.CharField(max_length=300)
    paper_language = models.CharField(max_length=20)
    paper_code = models.CharField(max_length=10, primary_key=True)
    paper_avgScore = models.CharField(max_length=2, blank=True, null=True)
    paper_accepted = models.NullBooleanField()
    def __str__(self):
    	return '%s %s' % (self.paper_code, self.paper_accepted)

class Reviewer(models.Model):
    reviewer_name = models.CharField(max_length=30)
    reviewer_surname = models.CharField(max_length=30)
    reviewer_id = models.CharField(max_length=10, primary_key=True)
    reviewer_institution = models.CharField(max_length=50)
    reviewer_email = models.EmailField(max_length=50)
    paper_code = models.ForeignKey('Paper', null=True)
    def __str__(self):
    	return '%s %s %s' % (self.reviewer_id, self.reviewer_name, self.reviewer_surname)

class Review(models.Model):
    review_score = models.CharField(max_length=2)
    reviewer_id = models.ForeignKey('Reviewer')
    paper_code = models.ForeignKey('Paper')
    def __str__(self):
    	return '%s %s %s' % (self.reviewer_id, self.review_score, self.paper_code)
    
class Author(models.Model):
    author_name = models.CharField(max_length=30)
    author_surname = models.CharField(max_length=30)
    author_id = models.CharField(max_length=10, primary_key=True)
    author_institution = models.CharField(max_length=50)
    author_country = models.CharField(max_length=50, blank=True)
    author_email = models.EmailField(max_length=50)
    def __str__(self):
    	return '%s %s %s' % (self.author_id, self.author_name, self.author_surname)
