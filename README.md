# BookPaths

BookPaths is a knowledge platform where users can share what they think might be a bookpath to master some subject. Its usage is recommended for people that has a learning approach based on reading.

A bookpath is a series of ordered steps through reading material that will guide a person to master a subject it is interested in.

---

## Functionalities

**Home page**: The homepage of the app will have an infinite scroll that will be filled with the recent bookpath submissions in chronological order. This page includes CSS animations so that the scroll seems more natural.

**Explore BookPaths**: The application will have a page where all the bookpaths can be explored. This page allows to filter and sort the bookpaths by their most relevant features like the category to which they belong, the number of followers or the number of steps that the bookpath has.

**Explore Books**: The application will have a page where all the books stored in the system can be explored. This page is similar to the one that allows to explore by bookpath. It allows filtering and sorting the books by their most relevant features like the title, author, number of pages or the number bookpaths in which it appears.

**Profile**: Registered users have a profile from where they can see the bookpaths that they are following and how the bookpaths that they have added are performing. The profile works as a control panel and not as a social network profile as users are not allowed to see other people profiles. The profile has the following sections (displayed as tabs):

* **Active Bookpaths**: An user can see the bookpahts that are currently active on his profile. Active bookpaths are those bookpaths the user follows that he has not yet started or is in the process of reading. The user will have the ability to start the bookpath, advance through its steps or to mark the bookpath as finished. If a user wants to leave a bookpath he can visit the bookpath page and unfollow it from there.
* **Finished Bookpaths**: An user can see the bookpahts that he has completed on his profile.
* **Your Contributions**: An user can see the bookpahts that he has submitted on his profile. This view will allow the user to see how his submissions are performing in a fast way.

**Contribute**: Users will be able to contribute to the platform by proposing the bookpaths that they find relevant for mastering a topic in one of the predefined categories. A bookpath must at least have a step (that is a book). The number of steps of a bookpath is currently limited to 5 due to API limitations. Once a valid bookpath is submitted, the user is redirected to the view of the bookpath.

**Bookpaths**: Each bookpath can be explored individually on its bookpath page. The following information of the bookpath will be displayed:

* Name of the bookpath.
* Category of the bookpath.
* Description of the bookpath.
* The number of steps that form the bookpath.
* The number of pages of all the books that form the bookpath.
* The author of the bookpath.
* The number of followers of the bookpath.
* The percentage of users that have completed the bookpath.
* An overview of all the books that compose the bookpath and the possibility to navigate over them.

**Follow Bookpaths**: From the bookpath page a logged in user will have the option to follow a bookpath. Once a user is following the bookpath, the bookpath page will reflect it on its numbers and the bookpath will appear in the user's profile.

**Book**: Each book stored in the system will have its own page. This page will display basic information about the book and a list of all the bookpaths in which the book has been included.

---

## Demo

A demo can be seen in the following video: lorem ipsum

---

## CS50’s Web Programming - Capstone Requirements

### Distinctiveness Requirements

Lorem ipsum

### Complexity Requirements

**Django**: The application has a Django backend that has more than 5 models as it can be seen in the `models.py` file of the `bookpaths_app` app. It uses most of all the other Django features seen during the course.

**JavaScript**: The application uses JS in different parts of its frontend. One example is the addition of the dynamic forms functions in the contribution part of the application. The JS code can be seen in the `static/bookpaths_app` folder of the `bookpaths_app` app. Other use of JS in the application is to perform the infinite scroll. The JS is in charge of performing the fetch requests that load the bookpaths and to add them to the homepage HTML.

### Repository Content

Lorem ipsum

### How to Run the Project

Lorem ipsum

#### Data Loading

In order to have sample data to work with, the repository includes mock data to bulk load, so that all the functionalities of the system can be tested. **Disclaimer: This is not something expected to be included in a regular repository, but an exception has been made so that the application can be properly evaluated**. In order to use this data the next steps must be followed:

1. Perform the migrations with the command `python manage.py migrate`.
2. Create a superuser with the command `python manage.py createsuperuser`.
3. Login to the admin panel and start importing the `.csv` files of the `data` directory in the following order:
   1. Users
   2. Categories
   3. Books
   4. BookPaths
   5. BookPaths Steps
4. Once this is done you can test the application with the mock data.

### Additional Stuff

The project makes use of the [Open Library API](https://openlibrary.org/developers/api) that has some restrictions on number of requests. Consider that if some action is abused in a short span of time an error can be returned by the API.

The project makes use of the Python library [Requests](https://requests.readthedocs.io/en/master/) in order to consume the above mentioned API. This library has been included in the `requirements.txt` file.

The project makes use of the Django application [django-filter](https://django-filter.readthedocs.io/en/stable/index.html) in order to allow filtering elements from the front of the application. This application has been included in the `requirements.txt` file.

The projects makes use of the Django application [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/) in order to be able to have more customizable widgets (used for filters). This library has been included in the `requirements.txt` file.

The project makes use of the jQuery plugin [Django Dynamic Formsets](https://github.com/elo80ka/django-dynamic-formset) to deal with the insertion of bookpaths. The source code of the plugin is included in the `static/bookpaths_app` folder of the app.

During the development of the project I have used the [Django import / export](https://django-import-export.readthedocs.io/en/stable/) library to bulk load data from files to test the application. It  has been included in the `requirements.txt` file.
