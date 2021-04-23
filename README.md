# BookPaths

BookPaths is a knowledge platform where users can share what they think might be a bookpath to master some subject. Its usage is recommended for people that have a learning approach based on reading.

A bookpath is a series of ordered steps through reading material that will guide a person to master a subject he/she is interested in.

---

## Functionalities

**Home page**: The homepage of the app will have an infinite scroll that will be filled with the recent bookpath submissions in chronological order. This page includes CSS animations so that the scroll seems more natural.

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

**Book**: Each book stored in the system will have its own page. This page will display basic information about the book and a list of all the bookpaths in which the book has been included.

**Explore BookPaths**: The application will have a page where all the bookpaths can be explored. This page allows to filter and sort the bookpaths by their most relevant features like the category to which they belong, the number of followers or the number of steps that the bookpath has.

**Explore Books**: The application will have a page where all the books stored in the system can be explored. This page is similar to the one that allows exploring by bookpath. It allows filtering and sorting the books by their most relevant features like the title, author, number of pages or the number bookpaths in which it appears.

**Follow Bookpaths**: From the bookpath page, a logged-in user will have the option to follow a bookpath. Once a user is following the bookpath, the bookpath page will reflect it on its numbers and the bookpath will appear in the user's profile.

**Profile**: Registered users have a profile from where they can see the bookpaths that they are following and how the bookpaths that they have added are performing. The profile works as a control panel and not as a social network profile as users are not allowed to see other people profiles. The profile has the following sections (displayed as tabs):

* **Active Bookpaths**: An user can see the bookpahts that are currently active on his profile. Active bookpaths are those bookpaths the user follows that he has not yet started or is in the process of reading. The user will have the ability to start the bookpath, advance through its steps or mark the bookpath as finished. If a user wants to leave a bookpath he can visit the bookpath page and unfollow it from there.
* **Finished Bookpaths**: An user can see the bookpahts that he has completed on his profile.
* **Your Contributions**: An user can see the bookpahts that he has submitted on his profile. This view will allow the user to see how his submissions are performing in a fast way.

**Contribute**: Users will be able to contribute to the platform by proposing the bookpaths that they find relevant for mastering a topic in one of the predefined categories. A bookpath must at least have a step (that is a book). The number of steps of a bookpath is currently limited to 5 due to API limitations. Once a valid bookpath is submitted, the user is redirected to the view of the bookpath.

---

## Demo

A demo can be seen in the following video: [CS50's Web Programming Course - Capstone - BookPaths](https://youtu.be/TOG2uRDa154)

---

## CS50’s Web Programming - Capstone Requirements

### Distinctiveness Requirements

The project is a knowledge platform where users can contribute with recommendations of reading steps they have used to master a topic.

* **It is not a social network** as users can not follow other users and cannot visit other users' profiles. The user profile works as a control panel for the user activity, nothing similar to that of a social network. This system supports neither social interaction nor personal relationships, two of the most relevant features of a social network.
* **It is not an e-commerce** as it does not try to sell any product, neither goods nor services.

### Complexity Requirements

**Django**: The application has a Django backend that has more than 5 models as it can be seen in the `models.py` file of the `bookpaths_app` app. It uses most of all the other Django features seen during the course.

**JavaScript**: The application uses JS in different parts of its frontend. One example is the addition of the dynamic forms functions in the contribution part of the application. The JS code can be seen in the `static/bookpaths_app` folder of the `bookpaths_app` app. Another use of JS in the application is to perform the infinite scroll. The JS is in charge of performing the fetch requests that load the bookpaths and adding them to the homepage HTML.

**Mobile Responsiveness**: The application is mobile-responsive and it has been tested with different screen sizes.

### Repository Content

The repository contains a folder structure similar to the one used in some of the projects of the course. The main directories and files are:

* `/bookpaths`: Contains the default files of the Django project. The files `/bookpaths/settings.py` and `/bookpaths/urls.py` have been modified to include the applications the project uses and their paths.
* `/bookpaths_app`: Contains all the code relative to the main application that handles the bookpaths. It contains the following relevant folders or files:
  * `/migrations`: Contains all the migrations needed to run the project.
  * `/static/bookpaths_app`: Includes both the `.css` files needed to style and animate the application and the `.js` files required for some of the functionalities of the application.
  * `/templates/bookpaths_app`: Includes all the `.html` files made up of Django templates that are the skeleton of the frontend of the application.
  * `/templatetags`: Includes custom tags for the Django templates.
  * `/*.py`: Files relevant for the Django application. The most relevant ones are `urls.py` that define the entry points of the application, `views.py` that define the behavior of the application and `models.py` that defines the mapping from the Django ORM to the database. `filters.py` and `forms.py` are also relevant files that define filters and forms used in the application so that single responsibility principle is achieved.
* `/data`: Contains sample data that can be used to initialize the project. A disclaimer and an explanation on how to use this data have been included in the [Data Loading](#data-loading) section.
* `requirements.txt`: Includes a freeze of all the dependencies of the project.

### How to Run the Project

In order to run the project, it is needed to have Python 3 installed. I recommend using version 3.6 as it was the development version. I also recommend using a virtual environment. The process once Python and venv are installed would be as follows:

1. Clone the repository or download the code.
2. Move to the cloned directory and create a virtual environment with the command `python3 -m venv env`.
3. Activate the virtual environment created with the command `source env/bin/activate`.
4. Install the required dependencies from the cloned repository with the command `pip install -r requirements.txt`.
5. Run the migrations so that the database is properly created with the command `python manage.py migrate`.
6. At this point the application will be ready to use but you can consider importing some mock data as explained in the [Data Loading](#data-loading) section.
7. Finally, run the server with the command `python manage.py runserver`. The system will be ready to use on port 8000 of your machine.

#### Data Loading

In order to have sample data to work with, the repository includes mock data to bulk load, so that all the functionalities of the system can be tested. **Disclaimer: This is not something expected to be included in a regular repository, but an exception has been made so that the application can be properly evaluated**. In order to use this data the next steps must be followed:

1. Perform the migrations with the command `python manage.py migrate`.
2. Create a superuser with the command `python manage.py createsuperuser`.
3. Log in to the admin panel and start importing the `.csv` files of the `data` directory in the following order:
   1. Users
   2. Categories
   3. Books
   4. BookPaths
   5. BookPaths Steps
4. Once this is done you can test the application with the mock data.

### Additional Stuff

The project makes use of the [Open Library API](https://openlibrary.org/developers/api) that has some restrictions on the number of requests. Consider that if some action is abused in a short span of time an error can be returned by the API.

The project makes use of the Python library [Requests](https://requests.readthedocs.io/en/master/) in order to consume the above-mentioned API. This library has been included in the `requirements.txt` file.

The project makes use of the Django application [django-filter](https://django-filter.readthedocs.io/en/stable/index.html) in order to allow filtering elements from the front of the application. This application has been included in the `requirements.txt` file.

The project makes use of the Django application [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/) in order to be able to have more customizable widgets (used for filters). This library has been included in the `requirements.txt` file.

The project makes use of the jQuery plugin [Django Dynamic Formsets](https://github.com/elo80ka/django-dynamic-formset) to deal with the insertion of bookpaths. The source code of the plugin is included in the `static/bookpaths_app` folder of the app.

During the development of the project I have used the [Django import / export](https://django-import-export.readthedocs.io/en/stable/) library to bulk load data from files to test the application. It has been included in the `requirements.txt` file.
