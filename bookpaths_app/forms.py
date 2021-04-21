from django import forms
from django.core.validators import RegexValidator

from .models import Category


class ContributionStepForm(forms.Form):
    book = forms.CharField(required=True, validators=[RegexValidator(regex='^.{10}$', message='All ISBNs need to have a length of 10', code='nomatch')], label="Book Step", max_length=10, widget=forms.TextInput(
        attrs={'placeholder': 'Insert the 10 ISBN', 'class': "form-control rounded m-2"}))

    def __init__(self, *arg, **kwarg):
        super(ContributionStepForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False


class ContributionForm(forms.Form):
    name = forms.CharField(label="BookPath Name", max_length=120, widget=forms.TextInput(
        attrs={'placeholder': 'Assign a meaningful name to the bookpath', 'class': "form-control rounded"}))
    description = forms.CharField(label="BookPath Description", max_length=240, widget=forms.Textarea(
        attrs={'placeholder': 'Provide a description for your bookpath', 'class': "form-control rounded", 'rows': 4}))
    category = forms.ModelChoiceField(
        label="BookPath Category", queryset=Category.objects.all(), initial=Category.objects.all().first)
