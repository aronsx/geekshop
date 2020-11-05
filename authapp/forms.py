from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        mode = User
        fields = ('usermane', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
