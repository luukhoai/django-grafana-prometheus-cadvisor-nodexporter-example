from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, \
    SetPasswordForm, PasswordChangeForm
from betterforms.multiform import MultiModelForm
from django.core.exceptions import ValidationError


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'htlfndr-input'})
        self.fields['password'].widget.attrs.update({'class': 'htlfndr-input'})

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise ValidationError('Password too short', code='inactive',)


class UserMultiModelForm(MultiModelForm):
    form_classes = {
        'login_form': UserLoginForm
    }