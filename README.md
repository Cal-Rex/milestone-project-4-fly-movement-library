# M O V E M E N T - L I B R A R Y
## F L Y - F U N C T I O N A L - F I T N E S S
___
# Table of Content
1. Introduction
2. Design
    - Project Brief
    - UX
    - Development Planes
        - Strategy
        - Scope
        - Structure
        - Skeleton
    - Color Scheme
    - Typography
    - Imagery & Media
3. Features
    - Design Features
    - Visual Features
    - Data Management
    - 404 / 500 Features
    - Future Development
4. Bugs
    - Resolved Bugs
    - Unresolved Bugs
5. Technologies
    - Languages
    - Frameworks
    - Libraries
    - Programs
6. Testing
7. Deployment
8. Credits
9. Acknowledgements

___

# I N T R O D U C T I O N
___

# D E S I G N

## Project Brief

The First version of this Project is to be submitted as an assessment piece as part of the Diploma in Full Stack Software Development (Advanced Front End) with Code Institute. As such, this project has to fulfil the following learning outcomes:

| **LO1** | Use an Agile methodology to plan and design a Full-Stack Web application using an MVC framework and related contemporary technologies |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1 |	Design a Front-End for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions. |
| 1.2 |	Implement custom HTML and CSS code to create a responsive Full-Stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data manipulation functions |
| 1.3 |	Build a database-backed MVC web application that allows users to store and manipulate data records about a particular domain. |
| 1.4 |	Design a database structure relevant for your domain, consisting of a minimum of one custom model. |
| 1.5 |	Use an Agile tool to manage the planning and implementation of all significant functionality |
| 1.6 |	Document and implement all User Stories and map them to the project within an Agile tool |
| 1.7 |	Write Python code that is consistent in style and conforms to the PEP8 style guide and validated HTML and CSS code. |
| 1.8 |	Include sufficient custom Python logic to demonstrate your proficiency in the language |
| 1.9 |	Include functions with compound statements such as if conditions and/or loops in your Python code |
| 1.10 | Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions). |
| 1.11 | Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility. |
| 1.12 | Document and implement all User Stories within the Agile tool and map them to the project goals |
| 1.13 | Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc.,created as part of the design process and its reasoning. Include diagrams created as part of the design process and demonstrate that these have been followed through to implementation |

| **LO2** | Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain. |
| ------- | ----------------- |
| 2.1 |	Develop the model into a usable database where data is stored in a consistent and well-organised manner. |
| 2.2 | Create functionality for users to create, locate, display, edit and delete records |
| 2.3 | All changes to the data should be notified to relevant user |
| 2.4 | Implement at least one form, with validation, that allows users to create and edit models in the backend |

| **LO3** | Identify and apply authorisation, authentication and permission features in a Full-Stack web application solution |
| ------- | ----------------------------------------------------------------------------------------------------------------- |
| 3.1 |	Apply role-based login and registration functionality |
| 3.2 |	The current login state is reflected to the user |
| 3.3 |	Users should not be permitted to access restricted content or functionality prior to role-based login. |

| **LO4** | Create manual and/or automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 4.1 |	Design and implement manual and/or automated Python test procedures to assess functionality,
usability, responsiveness and data management within the entire web application |
| 4.2 |	Design and implement manual and/or automated JavaScript test procedures to assess functionality,
usability, responsiveness and data management within the entire web application |
| 4.3 |	Document all implemented testing in the README. |

| **LO5** | Use a distributed version control system and a repository hosting service to document, develop and maintain a Full-Stack Web application using an MVC framework and related contemporary technologies |
| ------- | ------------------------------------------------------------ |
| 5.1 |	Use Git & GitHub for version control of a Full-Stack web application up to deployment, using commit messages to document the development process. |
| 5.2 |	Commit final code that is free of any passwords or security-sensitive information to the repository and the hosting platform |

| **LO6** | Deploy a Full-Stack Web application using an MVC framework and related contemporary technologies to a cloud-based platform |
| ------- | -------------------------------------------------------------------------------------------------------------------------- |
| 6.1 |	Deploy a final version of the Full-Stack application code to a cloud-based hosting platform and test to ensure it matches the development version |
| 6.2 |	Ensure that the final deployed code is free of commented out code and has no broken internal links |
| 6.3 |	Document the deployment process in a README file in English |
| 6.4 |	Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off |

| **LO7** | Understand and use object-based software concepts |
| ------- | ------------------------------------------------- |
| 7.1 |	Design a custom data model that fits the purpose of the project |


## UX

## Development Planes

### **Strategy Plane**

#### __User Stories__
1. Product Users
    - _"As a user, i want to log in and view specific workout/movement tutorials"_
    - _"As a user, i want to be able to search for specific workouts"_
    - _"As a user, i want to be able to bookmark movements for easy referencing"_
    - _"As a user, i want to know what other exercises compliment the ones i have bookmarked"_
    - _"As a user, i want to be able to create my own flow of movements to help keep me right suring my own training"_
    - _"As a user, if i am unsure of the name of a particular movement or a workout, i want to be able to search for it in the library"_
    - _"As a user, if i cant find the movement i am looking for, i want the app to give me suggestions based on my search"_
2. Stakeholders
    - _"As a business owner, i want to be able to see who has signed up to use this app"_
    - _"As a business owner, i want to know i have consent to access and use the data provided by users on sign up"_
    - _"As a business owner, i want to know what movements are most popular"_
    - _"As a business owner, i want to be able to promote my other products on this app seamlessly"_


### **Scope Plane**

### **Structure Plane**

#### __Table Diagrams__

User Details table model:
|     id     | first_name | last_name | username    | password  |   email    | T_and_Cs |
| ---------- | ---------- | --------- | ----------- | --------- | ---------- | -------- |
| PrimaryKey | CharField  | CharField | CharField   | TextField |    email   | Boolean  |
|     1      | Andy       | Roux      | exampleUser | Guest+1   | e@mail.com | True     |

MovementLibrary Table:
|     id     | movement_name |   vid_link    |   Slug    |       bookmarks       |
| ---------- | ------------- | ------------- | --------- | --------------------- |
| PrimaryKey |   TextField   |   TextField   | SlugField | ManyToManyField(User) |
|     1      |  Split Squat  | x.youtube.com |           |

Tags table:

| movement    | upper_body   | lower_body   | barbell | dumbbell | kettlebell | olympic | power   | strength | arms    | chest   | shoulders | back    |
| ----------- | ------- | ------- | ------- | -------- | ---------- | ------- | ------- | -------- | ------- | ------- | --------- | ------- |
| ForeignKey | Boolean | Boolean | Boolean | Boolean  | Boolean    | Boolean | Boolean | Boolean  | Boolean | Boolean | Boolean   | Boolean |
| MovementLibrary.id | True    | False   | True    | False    | False      | False   | True    | False    | True    | False   | True      | False   |


Bookmarks Table:
|  user_id   |                     bookmarked                   |
| ---------- | ------------------------------------------------ |
| ForeignKey | [list, of, MovementLibrary.ids, as, ForeignKeys] |
|     1      |                   [1, 3, 6, 22, 2]               |

Flows Table:
|  user_id   |                              flow                                 |
| ---------- | ----------------------------------------------------------------- |
| ForeignKey | {'named flow': [list, of, MovementLibrary.ids, as, ForeignKeys],} |
|     1      |         {'International Chest Day': [3, 5, 8, 7, 4, 2],}          |

#### __Entity Relationship Diagram__

A movement:
| Key | Name |      Type      |
| --- | ---- | -------------- |
|     | Name | Charfield[100] |
|     | link | string         |
|     | slug |                |

### **Skeleton Plane**

## Colour Scheme

## Typography

## Imagery & Media
___

# B U G S

## Resolved bugs
- Initial heroku build failed, failed to compile python app
    - Error thrown:
    ```
    lib/zoneinfo_module.c:600:19: error: ‘_PyLong_One’ undeclared (first use in this function); did you mean ‘_PyLong_New’?
               600 |             one = _PyLong_One;
                   |                   ^~~~~~~~~~~
                   |                   _PyLong_New
             lib/zoneinfo_module.c:600:19: note: each undeclared identifier is reported only once for each function it appears in
             error: command '/usr/bin/gcc' failed with exit code 1
    ```
    - Solution: replace stock package install of `backports.zoneinfo==0.2.1` with `backports.zoneinfo;python_version<"3.9"` in requirements.txt
- 403 Error when accessing Admin panel
    - error thrown:"csrf verification failed. request aborted."
    - Solution: Add CSRF_TRUSTED_ORIGINS list variable with permitted domains to settings.py
- JQuery functions producing type error:
    - error caused by cloudinary having insufficient capacity to run size of static files on free subscription plan. uninstalled package and now pulling script from CDN

## Un-resolved bugs
- iframe in index will not respond to style rules set in style.css
    - had to implement style rules directly into index.html
- cant remove header from youtube video
    - can be done potentially by using jquery:
        - https://stackoverflow.com/questions/583753/using-css-to-affect-div-style-inside-iframe/30545122#30545122
        -   ``` js
            $('iframe').load( function() {
                $('iframe').contents().find("head")
                    .append($("<style type='text/css'>  .my-class{display:none;}  </style>"));
            });
            ```
        - will address fix later
- Youtube videos will always fail on first load:
    - known issue by google and community, currently google are fixing
        - https://issuetracker.google.com/issues/249707272?pli=1
    - javascript and API override attempted, but couldn't get it to work
        - https://stackoverflow.com/questions/19410789/youtube-player-api-with-loop
    - client has alternative hosting service already set up. Will use this instead.
- when a 1rm is entered, movement becomes un-bookmarked
___

# C R E D I T S

- https://www.csestack.org/django-default-user-model-fields/
- https://stackoverflow.com/questions/44109/extending-the-user-model-with-custom-fields-in-django
- https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/
- https://realpython.com/customize-django-admin-python/
- https://dev.to/thepylot/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
- https://medium.com/@inem.patrick/django-database-integrity-foreignkey-on-delete-option-db7d160762e4
- https://www.w3schools.com/css/css_form.asp
- https://developer.mozilla.org/en-US/docs/Web/CSS/::placeholder
- https://yoast.com/how-to-make-youtube-videos-responsive/
- https://getbootstrap.com/docs/4.0/getting-started/introduction/
- https://www.google.com/
- https://dev.to/thepylot/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
- https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message
- https://stackoverflow.com/questions/47471970/django-how-to-pull-a-logged-in-users-data-from-a-database-table
- https://stackoverflow.com/questions/69390875/django-filter-data-in-table-based-on-value-from-another-table
- https://stackoverflow.com/questions/67553372/bootstrap-5-off-canvas-left-to-right
- https://www.w3schools.com/css/css_rwd_videos.asp
- https://www.scaler.com/topics/html-video-autoplay/
- https://www.cincopa.com/blog/how-to-embed-youtube-videos-without-showing-controls/
- https://www.youtube.com/watch?v=K8YrX15e31s
- https://stackoverflow.com/questions/25779966/youtube-iframe-loop-doesnt-work
- https://stackoverflow.com/questions/40642374/how-to-disable-full-screen-on-youtube-iframe
- https://www.geeksforgeeks.org/booleanfield-django-models/
- https://docs.djangoproject.com/en/4.2/ref/csrf/
- https://stackoverflow.com/questions/29573163/django-admin-login-suddenly-demanding-csrf-token
- https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins
- https://stackoverflow.com/questions/1479206/django-templating-how-to-access-properties-of-the-first-item-in-a-list

