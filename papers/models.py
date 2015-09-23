from django.db import models

# Create your models here.
class Chairperson(models.Model):
    cp_username = models.CharField(max_length=30)
    cp_password = models.CharField(max_length=30)

class CommitteeMember(models.Model):
    cm_name = models.CharField(max_length=30)
    cm_surname = models.CharField(max_length=30)
    cm_institution = models.CharField(max_length=30)
    cm_email = models.CharField(max_length=30)

class Paper(models.Model):
    paper_authorName = models.CharField(max_length=30)
    paper_submissionDate = models.CharField(max_length=30)
    paper_abstract = models.CharField(max_length=30)
    paper_language = models.CharField(max_length=30)
    paper_code = models.CharField(max_length=30)
    paper_reviewCode = models.CharField(max_length=30)
    paper_avgScore = models.CharField(max_length=30)

class Reviewer(models.Model):
    reviewer_name = models.CharField(max_length=30)
    reviewer_surname = models.CharField(max_length=30)
    reviewer_institution = models.CharField(max_length=30)
    reviewer_email = models.CharField(max_length=30)
    reviewer_paperCode = models.CharField(max_length=30)
    reviewer_reviewCode = models.CharField(max_length=30)

class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
