import datetime

from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
# from django.utils import timezone

# Our models.
class MyUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('Users must include username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given username, email and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        max_length=255,
        unique=True,
        )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        )
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    is_author = models.BooleanField(default=True, verbose_name='Is an Author')
    is_reviewer = models.BooleanField(default=False, verbose_name='Is a Reviewer')
    is_cm = models.BooleanField(default=False, verbose_name='Is a Committee Member')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # role = models.CharField(max_length=20)
    # institution = models.CharField(max_length=50)
    # country = models.CharField(max_length=50)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their full name
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        #I THINK THIS IS WHERE WE WILL HAVE SOME IF STATEMENTS
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# def new_user_reciever(sender, instance, created, *args, **kwargs):
#     if created:
#         new_profile, is_created = UserProfile.objects.created(user=instance)
#         print (new_profile, is_created)

# post_save.connect(new_user_reciever, sender=MyUser)

class Paper(models.Model):
    user = models.OneToOneField(MyUser)
    title = models.CharField(max_length=100)
    paper_submissionDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    abstract = models.TextField(max_length=300)
    language = models.CharField(max_length=20)
    paper_file = models.FileField(upload_to='paper_list/%Y/%m/%d')
    paper_code = models.AutoField(primary_key=True)
    paper_avgScore = models.CharField(max_length=2, blank=True, null=True)
    paper_accepted = models.NullBooleanField()
    def __str__(self):
    	return '%s' % (self.paper_code) #self.user.username

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
    user = models.OneToOneField(MyUser)
    paper_code = models.ForeignKey('Paper')
    comments = models.TextField(max_length=300)
    def __str__(self):
    	return '%s' % (self.paper_code)
    

