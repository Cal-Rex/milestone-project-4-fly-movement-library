# M O V E M E N T - L I B R A R Y
## F L Y - F U N C T I O N A L - F I T N E S S
___
# Table of Content
1. Introduction
2. Design
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
