from django import forms


class LoginForm(forms.Form):
    """class for the login form"""
    email = forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = "form-control"
