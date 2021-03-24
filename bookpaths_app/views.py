from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import RegexValidator
from django.db import IntegrityError
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import BookPath, Category, User


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
        attrs={'placeholder': 'Write your new post', 'class': "form-control rounded", 'rows': 4}))
    category = forms.ModelChoiceField(
        label="BookPath Category", queryset=Category.objects.all(), initial=Category.objects.all().first)


def categories(request):
    return render(request, "bookpaths_app/index.html")


def index(request):
    return render(request, "bookpaths_app/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profile"))
        else:
            return render(request, "bookpaths_app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "bookpaths_app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "bookpaths_app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "bookpaths_app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "bookpaths_app/register.html")


@login_required
def profile(request):
    active_bookpaths = request.user.follows.filter(
        status=0) | request.user.follows.filter(status=1)
    finished_bookpaths = request.user.follows.filter(status=2)
    contributions = BookPath.objects.filter(author=request.user)

    return render(request, "bookpaths_app/profile.html", {
        'active_bookpaths': active_bookpaths,
        'finished_bookpaths': finished_bookpaths,
        'contributions': contributions,
    })


@login_required
def contribute(request):
    StepFormSet = formset_factory(ContributionStepForm, min_num=1, max_num=5)

    if request.method == 'POST':
        contribution_form = ContributionForm(request.POST)
        contribution_step_formset = StepFormSet(request.POST)

        if contribution_form.is_valid() and contribution_step_formset.is_valid():
            pass
    else:
        contribution_form = ContributionForm()
        contribution_step_formset = StepFormSet()

    return render(request, "bookpaths_app/contribute.html", {
        'contribution_form': contribution_form,
        'contribution_step_formset': contribution_step_formset,
    })
