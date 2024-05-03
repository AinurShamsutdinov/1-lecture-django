from datetime import datetime

from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_name(self):
        # bad example duplication of the parameter min_length
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Name should be longer than 3 symbols.')
        return name

    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team')) or email.endswith('corp.mail.ru'):
            raise forms.ValidationError('Use corporative mail')
        return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.today())
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter user name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.today(), widget=forms.DateInput(attrs={'class': 'form_control', 'type':'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
    image = forms.ImageField()
