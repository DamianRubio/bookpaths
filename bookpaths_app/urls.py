from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("contribute", views.contribute, name="contribute"),
    path("categories", views.categories, name="categories"),
    path("bookpath/<int:bookpath_id>", views.bookpath, name="bookpath"),
    path("book/<str:book_isbn>", views.book, name="book"),
]
