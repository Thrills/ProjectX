import datetime

from django.db import models
# from django.utils import timezone

# Our models.

class RegisteredUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30,)
    roles = (  # Provides users with a specific choice
                 ('Author', 'Author'),
                 ('Reviewer', 'Reviewer'),
                 ('Commiteee Member', 'Commiteee Member'),
                 )
    role = models.CharField(max_length=20, choices=roles, blank=True)
    institution = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def __str__(self):
      return '%s' % (self.id)

class Paper(models.Model):
    id = models.ForeignKey('RegisteredUser')
    title = models.CharField(max_length=100)
    paper_submissionDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    abstract = models.CharField(max_length=300)
    language = models.CharField(max_length=20)
    paper_file = models.FileField(upload_to='paper_list/%Y/%m/%d')
    paper_code = models.AutoField(primary_key=True)
    paper_avgScore = models.CharField(max_length=2, blank=True, null=True)
    paper_accepted = models.NullBooleanField()
    def __str__(self):
    	return '%s' % (self.paper_code)

class Review(models.Model):
    review_score = (  # Provides users with a specific choice
                 ('1', '1'),
                 ('2', '2'),
                 ('3', '3'),
                 ('4', '4'),
                 ('5', '5'),
                 ('6', '6'),
                 ('7', '7'),
                 ('8', '8'),
                 ('9', '9'),
                 ('10', '10'),
                 )
    review_score = models.CharField(max_length=2, choices=review_score, blank=True)
    id = models.ForeignKey('RegisteredUser', primary_key=True)
    paper_code = models.ForeignKey('Paper')
    comments = models.CharField(max_length=300)
    def __str__(self):
    	return '%s' % (self.paper_code)
    

