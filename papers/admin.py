from django.contrib import admin

from .forms import PaperForm, ReviewForm, UserChangeForm, UserCreationForm, PaperChangeForm

from .models import Paper, Review, MyUser

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Read only means we do not display the password


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_admin', 'is_author', 'is_reviewer', 'is_cm')
    list_filter = ('is_admin', 'is_author', 'is_reviewer', 'is_cm')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','role', 'institution', 'country')}),
        ('Permissions', {'fields': ('is_admin', 'is_author', 'is_reviewer', 'is_cm')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'first_name', 'last_name', 'role', 'institution', 'country')}
        ),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


class PaperAdmin(admin.ModelAdmin):
    list_display = ["__str__", "username", "paper_submissionDate", "paper_avgScore", "paper_accepted"]         # Different data the Admin will be able to view
    form = PaperChangeForm
    add_form = PaperForm
    
admin.site.register(Paper, PaperAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["__str__", "username", "review_score"]
    form = ReviewForm
    
admin.site.register(Review, ReviewAdmin)


