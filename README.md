# Book Paths

Book Paths is a knowledge platform where users can share what they think might be a bookpath to master some subject. Its usage is recommended for people that has a learning approach based on reading.

A bookpath is a series of ordered steps through reading material that will guide a person to master a subject it is interested in.

---
## Functionalities

**Profile**: Registered users have a profile from where they can see the bookpaths that they are following and how the bookpaths that they have added are performing. The profile works as a control panel and not as a social network profile as users are not allowed to see other peoples profiles.

**Contribute**: Users will be able to contribute to the platform by proposing the bookpaths that they find relevant for mastering a topic in one of the predefines categories. A bookpath must at least have a step (that is a book). The number of steps of a bookpath is currently limited to 5 due to API limitations.

---
## Demo

A demo can be seen in the following video: lorem ipsum

---
## CS50’s Web Programming - Capstone Requirements

### Distinctiveness Requirements

Lorem ipsum

### Complexity Requirements

**Django**: The application has a Django backend that has up to 5 models as it can be seen in the `models.py` file of the `bookpaths_app` app. It uses most of all the other Django features seen during the course.

**JavaScript**: The application uses JS in different parts of its frontend. One example is the addition of the dynamic forms functions in the contribution part of the application. The JS code can be seen in the `static/bookpaths_app` folder of the `bookpaths_app` app.

### Repository Content

Lorem ipsum

### How to Run the Project

Lorem ipsum

### Additional Stuff

The project makes use of the [Open Library API](https://openlibrary.org/developers/api) that has some restrictions on number of requests. Consider that if some action is abused in a short span of time an error can be returned by the API.

The project makes use of the Python library [Pillow](https://pillow.readthedocs.io/en/stable/) to deal with the book covers. This library has been included in the `requirements.txt` file.

The project makes use of the jQuery plugin [Django Dynamic Formsets](https://github.com/elo80ka/django-dynamic-formset) to deal with the insertion of bookpaths. The source code of the plugin is included in the `static/bookpaths_app` folder of the app.

During the development of the project I have used the [Django import / export](https://django-import-export.readthedocs.io/en/stable/) library to load data from files. It  has been included in the `requirements.txt` file.
