from authorization.models import UserProfile
from django import forms


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'name',
            'age',
            'country'
        )
