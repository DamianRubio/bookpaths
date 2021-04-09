import requests
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import RegexValidator
from django.db import IntegrityError
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import (Book, BookPath, BookPathFollow, BookPathStep, Category,
                     User)


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

    if request.method == 'POST':
        if 'path_start' in request.POST:
            bookpath_follow_id = request.POST.get('bookpath-follow')
            bookpath_follow = get_object_or_404(BookPathFollow, id=bookpath_follow_id)
            bookpath_follow.status = 1
            bookpath_follow.current_step +=1
            bookpath_follow.save()
        elif 'path_next' in request.POST:
            bookpath_follow_id = request.POST.get('bookpath-follow')
            bookpath_follow = get_object_or_404(BookPathFollow, id=bookpath_follow_id)
            bookpath_follow.current_step += 1
            bookpath_follow.save()
        elif 'path_finished' in request.POST:
            bookpath_follow_id = request.POST.get('bookpath-follow')
            print(bookpath_follow_id)
            bookpath_follow = get_object_or_404(BookPathFollow, id=bookpath_follow_id)
            bookpath_follow.status = 2
            bookpath_follow.save()

    active_bookpaths = request.user.follows.filter(
        status=0) | request.user.follows.filter(status=1)
    finished_bookpaths = request.user.follows.filter(status=2)
    contributions = BookPath.objects.filter(author=request.user)

    return render(request, "bookpaths_app/profile.html", {
        'active_bookpaths': active_bookpaths,
        'finished_bookpaths': finished_bookpaths,
        'contributions': contributions,
    })


def find_book(isbn_10):
    if Book.objects.filter(isbn_10=isbn_10).exists():
        return Book.objects.get(isbn_10=isbn_10)
    else:
        try:
            response = requests.get(
                f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn_10}&jscmd=details&format=json')
            book_data = response.json().get(f'ISBN:{isbn_10}')
            cover = book_data.get('thumbnail_url').replace('-S.jpg', '-M.jpg')
            new_book = Book(isbn_10=book_data.get('details').get('isbn_10')[0], isbn_13=book_data.get('details').get('isbn_13')[0], title=book_data.get('details').get('title'), publishers=book_data.get(
                'details').get('publishers')[0], number_of_pages=book_data.get('details').get('number_of_pages'), author=book_data.get('details').get('authors')[0].get('name'), cover=cover)
            new_book.save()
            return new_book
        except:
            raise Exception(f'The ISBN {isbn_10} can not be found')


def store_steps(bookpath, books_in_bookpath):
    for book in books_in_bookpath:
        bookpath_step = BookPathStep(book=book, bookpath=bookpath)
        bookpath_step.save()


@login_required
def contribute(request):
    StepFormSet = formset_factory(ContributionStepForm, min_num=1, max_num=5)
    list(messages.get_messages(request))

    if request.method == 'POST':
        contribution_form = ContributionForm(request.POST)
        contribution_step_formset = StepFormSet(request.POST)

        if contribution_form.is_valid() and contribution_step_formset.is_valid():
            books_in_bookpath = []
            for f in contribution_step_formset:
                cd = f.cleaned_data
                try:
                    books_in_bookpath.append(find_book(cd.get('book')))
                except Exception as e:
                    messages.error(request, e)
                    return render(request, "bookpaths_app/contribute.html", {
                        'contribution_form': contribution_form,
                        'contribution_step_formset': contribution_step_formset,
                    })
            bookpath_cd = contribution_form.cleaned_data
            category = Category.objects.get(name=bookpath_cd.get('category'))
            bookpath = BookPath(name=bookpath_cd.get('name'), description=bookpath_cd.get(
                'description'), category=category, author=request.user)
            bookpath.save()
            store_steps(bookpath, books_in_bookpath)
            return HttpResponseRedirect(reverse("bookpath", args=(bookpath.id, )))
    else:
        contribution_form = ContributionForm()
        contribution_step_formset = StepFormSet()

    return render(request, "bookpaths_app/contribute.html", {
        'contribution_form': contribution_form,
        'contribution_step_formset': contribution_step_formset,
    })


def bookpath(request, bookpath_id):

    bookpath = get_object_or_404(BookPath, id=bookpath_id)

    if request.method == 'POST':
        if 'path_follow' in request.POST:
            bookpath_follow = BookPathFollow(
                bookpath=bookpath, follower=request.user)
            bookpath_follow.save()
        elif 'path_unfollow' in request.POST:
            bookpath_follow = BookPathFollow.objects.get(
                bookpath=bookpath, follower=request.user)
            bookpath_follow.delete()
        bookpath.refresh_from_db()

    bookpath_steps = BookPathStep.objects.filter(bookpath=bookpath)
    total_pages = sum([step.book.number_of_pages for step in bookpath_steps])
    is_following = False

    if request.user.is_authenticated:
        is_following = BookPathFollow.objects.filter(
            bookpath=bookpath, follower=request.user).exists()

    return render(request, "bookpaths_app/bookpath.html", {
        "bookpath": bookpath,
        "bookpath_steps": bookpath_steps,
        "total_pages": total_pages,
        "is_following": is_following,
    })


def book(request, book_isbn):
    pass
