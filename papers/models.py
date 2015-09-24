from django.db import models

# Create your models here.
class Chairperson(models.Model):
    cp_username = models.CharField(max_length=30)
    cp_password = models.CharField(max_length=30)

class CommitteeMember(models.Model):
    cm_name = models.CharField(max_length=30)
    cm_surname = models.CharField(max_length=30, primary_key=True)
    cm_institution = models.CharField(max_length=50)
    cm_email = models.EmailField(max_length=50)

class Paper(models.Model):
    paper_authorNames = models.CharField(max_length=100)
    paper_author_id = models.CharField(max_length=10, primary_key=True)
    paper_submissionDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    paper_submissionUpdate = models.DateTimeField(auto_now=True, auto_now_add=False)
    paper_abstract = models.CharField(max_length=300)
    paper_language = models.CharField(max_length=20)
    paper_code = models.IntegerField(max_length=10, primary_key=True)
    paper_reviewCode = models.IntegerField(max_length=10)
    paper_avgScore = models.IntegerField(max_length=2, blank=True, null=True)
    paper_accepted = models.NullBooleanField()
    author = models.ForeignKey('Author') # Multiple papers can have multiple authors, but only one person will submit
    reviewer = models.ManyToManyField('Reviewer') #Papers can have many reviewers and vice versa

class Reviewer(models.Model):
    reviewer_name = models.CharField(max_length=30)
    reviewer_surname = models.CharField(max_length=30)
    reviewer_id = models.IntegerField(max_length=10, primary_key=True)
    reviewer_institution = models.CharField(max_length=50)
    reviewer_email = models.EmailField(max_length=50)
    reviewer_paperCode = models.IntegerField(max_length=10)
    reviewer_reviewCode = models.IntegerField(max_length=10, blank=True, null=True)
    review = models.OneToOneField('Review') # a Review can only belong to one reviewer

class Review(models.Model):
    review_score = models.IntegerField(max_length=2)
    review_reviewCode = models.IntegerField(max_length=10, primary_key=True)
    review_reviewer_id = models.IntegerField(max_length=10)
    review_paperCode = models.IntegerField(max_length=10)
    reviewer = models.ForeignKey('Reviewer') # Reviewer can have many reviews

class Author(models.Model):
    author_name = models.CharField(max_length=30)
    author_surname = models.CharField(max_length=30)
    author_id = models.CharField(max_length=10, primary_key=True)
    author_institution = models.CharField(max_length=50)
    author_country = models.CharField(max_length=50, blank=True)
    author_email = models.EmailField(max_length=50)
