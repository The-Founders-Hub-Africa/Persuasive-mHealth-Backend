from django.contrib import admin
from django import forms
# from django.contrib.auth import get_user_model
# Users=get_user_model()
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import Medical_practitional_Meta_Data, Patient,User

# Register your models here

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email',)
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
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
        model = User
        fields = ('phone_number','email', 'password', 'is_active', 'is_admin')
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('full_name','email','phone_number', 
                    'verified_number','verified_email','patient_count','is_admin','is_staff')
    list_filter = ('is_admin',)
    # actions = [make_manager,]
    actions = []
    fieldsets = (
    (None, {'fields': ('full_name','email','phone_number','patient_count','specialization','verified_number',
                       'api_number','password',
    'is_active')}),
    ('Permissions', {'fields': ('is_admin',"staff")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('full_name','phone_number',
               'specialization',
               'email','password1', 'password2')}
    ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User,UserAdmin)

admin.site.register(Patient)
admin.site.register(Medical_practitional_Meta_Data)

