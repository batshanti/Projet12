from django import forms
from django.contrib import admin
from user.models import User


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'team',
            'is_active',
            'is_staff',
            'is_superuser'
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'team')

    # fieldsets = (
    #     (
    #         'User information',
    #         {'fields': (
    #             'username',
    #             'first_name',
    #             'last_name',
    #             'email',
    #             'password',
    #             'team',
    #             'is_active',
    #             'is_staff',
    #             'is_superuser'
    #         )}
    #     ),
    # )
    search_fields = ('email',)


admin.site.register(User, UserAdmin)
