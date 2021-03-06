from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Paper, Review, MyUser


class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    roles = (  # Provides users with a specific choice
                 ('Author', 'Author'),
                 ('Reviewer', 'Reviewer'),
                 ('Commiteee Member', 'Commiteee Member'),
                 )
    role = forms.ChoiceField(roles)
    institution = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            exists = MyUser.objects.get(username=username)
            raise forms.ValidationError("This username is taken")
        except MyUser.DoesNotExist:
            return username
        except:
            raise forms.ValidationError("There was an error, please try again")


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("This email is taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("There was an error, please try again")


    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name


    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name


    def clean_role(self):
        role = self.cleaned_data.get('role')
        return role


    def clean_institution(self):
        institution = self.cleaned_data.get('institution')
        return institution


    def clean_country(self):
        country = self.cleaned_data.get('country')
        return country

# Used in admin
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


    class Meta:
        model = MyUser
        fields = ('email', 'username', 'first_name', 'last_name')


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()


    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username', 'first_name', 'last_name' , 'is_active', 'is_admin', 'is_author', 'is_reviewer', 'is_cm')


    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'abstract', 'language', 'paper_file']


class PaperChangeForm(forms.ModelForm):
    """A form for updating papers. Includes all the fields on
    the paper.
    """

    class Meta:
        model = Paper
        fields = ('username', 'title', 'abstract', 'language', 'paper_file', 'paper_avgScore', 'paper_accepted')


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['paper_code', 'review_score', 'comments']
    # review form takes fields from the model review


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())
    # log in requires only username and password
    