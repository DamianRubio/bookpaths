from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bookpaths", views.bookpaths, name="bookpaths"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("contribute", views.contribute, name="contribute"),
    path("explore/bookpaths", views.explore_bookpaths, name="explore_bookpaths"),
    path("explore/books", views.explore_books, name="explore_books"),
    path("bookpath/<int:bookpath_id>", views.bookpath, name="bookpath"),
    path("book/<str:book_isbn>", views.book, name="book"),
]
