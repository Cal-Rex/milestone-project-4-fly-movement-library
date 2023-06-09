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


The Fly Movement Library is a web app that aims to streamline the accessability to online content that guides functional weightlifting and fitness, coached and promoted by [The Fly Project](https://fly.fit) in Glasgow, Scotland.

Prior to the concept of this App, The Fly Project created a library of movements (to be accessed on their website) which users could access to help guide them through self-led training outside of a class or to help supplement coaching.

The library in it's current state, is going through a revamp online. This project aims to demonstrate the possibilities of the Movement Library catalysing it's own value in the form of its own app, with a user experience that focuses on the personal development of the user.

The initial version of this app aims to provide the service of users being able to seemlessly search for particular movements, regardless of knowing correct movement terminology. The app should also be able to recommend similar movements - or - other movements that compliment a searched movement. Additionally, users will also be able to record and track their one rep max (how much weight a user can lift in a specific movement through one iteration of the movement safely) on all weighted movements - This is an important feature for users training in functional weightlifting, as this figure is used to calculate ideal/safe weights for certain movements conducted in specific rep ranges in functional training.

**This project is the fourth of the five projects to be created for the Diploma in Full Stack Software Development (Advanced Front End)**

Project scope:
>_"In this project, you'll build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset."_

Based on this scope this project will deliver the following:
- Build a full-stack site based on business logic to control a centrally owned dataset
- a site that is mediated by a role-based authentication mechanism
    - depending on the nature of the role, users have options to conduct full CRUD functionality on specific aspects the aformentioned dataset (admin/user)
- The site will employ the use of external libraries and frameworks to create a robust experience via the use of HTML, CSS, Javascript and Python languages
<br>
<br>
___


# D E S I G N

## Project Brief

The First version of this Project is to be submitted as an assessment piece as part of the Diploma in Full Stack Software Development (Advanced Front End) with Code Institute. As such, this project has to fulfil the following learning outcomes:

| **LO1** | Use an Agile methodology to plan and design a Full-Stack Web application using an MVC framework and related contemporary technologies | achieved by: |
| ------- | ------------ |------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1 |	Design a Front-End for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions. |    |
| 1.2 |	Implement custom HTML and CSS code to create a responsive Full-Stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data manipulation functions |  multiple HTML pages as templates called by Django framework  |
| 1.3 |	Build a database-backed MVC web application that allows users to store and manipulate data records about a particular domain. | Users can Create, read, update and Delete their own dated 1-rep max records, as well as view the whole history |
| 1.4 |	Design a database structure relevant for your domain, consisting of a minimum of one custom model. | database consists of 5 custom tables |
| 1.5 |	Use an Agile tool to manage the planning and implementation of all significant functionality | used github issues/milestones/projects features to manage planning and implementation |
| 1.6 |	Document and implement all User Stories and map them to the project within an Agile tool | Github features (as above) used |
| 1.7 |	Write Python code that is consistent in style and conforms to the PEP8 style guide and validated HTML and CSS code. | code validated using pylint and checkers |
| 1.8 |	Include sufficient custom Python logic to demonstrate your proficiency in the language | see all .py files   |
| 1.9 |	Include functions with compound statements such as if conditions and/or loops in your Python code | see .py and .html files   |
| 1.10 | Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions). | followed conventions |
| 1.11 | Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility. | followed conventions |
| 1.12 | Document and implement all User Stories within the Agile tool and map them to the project goals | see github projects |
| 1.13 | Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc.,created as part of the design process and its reasoning. Include diagrams created as part of the design process and demonstrate that these have been followed through to implementation | see Design section below |

| **LO2** | Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain. | achieved by: |
| ------- | ----------------- | ------------ |
| 2.1 |	Develop the model into a usable database where data is stored in a consistent and well-organised manner. | tables structured and implemented where admin access is user friendly |
| 2.2 | Create functionality for users to create, locate, display, edit and delete records | 1-rep max records feature |
| 2.3 | All changes to the data should be notified to relevant user |    |
| 2.4 | Implement at least one form, with validation, that allows users to create and edit models in the backend | 2 forms for 1 rm data, sugn up form implemented through allauth plugin |

| **LO3** | Identify and apply authorisation, authentication and permission features in a Full-Stack web application solution | achieved by: |
| ------- | ----------------------------------------------------------------------------------------------------------------- | ------------ |
| 3.1 |	Apply role-based login and registration functionality |  used Allauth plugin  |
| 3.2 |	The current login state is reflected to the user | UI and app only available to authenticated users, otherwise only login screen accessible |
| 3.3 |	Users should not be permitted to access restricted content or functionality prior to role-based login. | see above |

| **LO4** | Create manual and/or automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies |  achieved by: |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| 4.1 |	Design and implement manual and/or automated Python test procedures to assess functionality, usability, responsiveness and data management within the entire web application |    |
| 4.2 |	Design and implement manual and/or automated JavaScript test procedures to assess functionality, usability, responsiveness and data management within the entire web application |    |
| 4.3 |	Document all implemented testing in the README. |    |

| **LO5** | Use a distributed version control system and a repository hosting service to document, develop and maintain a Full-Stack Web application using an MVC framework and related contemporary technologies | achieved by: |
| ------- | ------------------------------------------------------------ | ------------ |
| 5.1 |	Use Git & GitHub for version control of a Full-Stack web application up to deployment, using commit messages to document the development process. |    |
| 5.2 |	Commit final code that is free of any passwords or security-sensitive information to the repository and the hosting platform |    |

| **LO6** | Deploy a Full-Stack Web application using an MVC framework and related contemporary technologies to a cloud-based platform | achieved by: |
| ------- | -------------------------------------------------------------------------------------------------------------------------- | ------------ |
| 6.1 |	Deploy a final version of the Full-Stack application code to a cloud-based hosting platform and test to ensure it matches the development version |
| 6.2 |	Ensure that the final deployed code is free of commented out code and has no broken internal links |    |
| 6.3 |	Document the deployment process in a README file in English |    |
| 6.4 |	Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off |    |

| **LO7** | Understand and use object-based software concepts | achieved by: |
| ------- | ------------------------------------------------- | ------------ |
| 7.1 |	Design a custom data model that fits the purpose of the project | see models.py |


## UX

### Research

Training apps are absolutely not a new thing in the App market and economy, and there is an abundance of products out there to draw inspiration from. The idea for this project however, was inspired mainly by the App - [GOWOD](https://www.gowod.app/), which is an app that focuses on stretching and mobility, concepts that pair well and draw close parrallels with functional weightlifting:
|                                                            |                          GOWOD UI                          |               |
| :--------------------------------------------------------: | :--------------------------------------------------------: | :------------------------------------: |
| ![gowod-preview-1](/static/media/readme-media/gowod-1.jpg) | ![gowod-preview-2](/static/media/readme-media/gowod-2.jpg) | ![gowod-preview-3](/static/media/readme-media/gowod-3.jpg) |

- The app is excellent in terms of responsiveness and is very user friendly
- it provides fantastic tailored information and data to the user based on the information the user enters into the app
- it's serach function however is very direct, and isn't necessarily friendly to users who are new to training, or lack knowledge of movement terminology.


<br>

## Development Planes

### **Strategy Plane**

#### __User Stories__
1. Product Users
    - _"as a User i want to be able to edit any 1-rep max records i have entered in the event that i was bad at math at the time of recording"_
    - _"As a user, i want to be able to log in so that i can view specific workout/movement tutorials"_
    - _"As a user, I want to be able to search for specific workouts, so that I can easily find the movement I am looking for"_
    - _"As a User, I want to be able to Bookmark movements, so that I can refer to them easily at a later date"_
    - _"As a User, I want to be able to know what other exercises compliment the ones i have bookmarked, so that I can expand my training"_
    - _"As a User, I want to be able to create my own flow of movements, so that ** i can keep me right during my own training**"_
    - _"As a User, i want to be able to search for movements even if i am unsure of their names so that I can find my moevements easily without having to know all the correct terminology"_
    - _"As a user, I want to be able to have recommendations from my searches, so that if I cant find the movement I am looking for, I have alternatives to try"_
    - _"As a User i want to be able to add my own personal notes to a movement, for my own reference so that i can keep track of different aspects of my workout and training"_
    - _"As a User I want to be able to record my own 1-rep maxes in the app and date them so that I can track my progression"_
    - _"as a User I want to be able to edit any notes I attach to a workout so that I can amend my notes to have relevant information when I am training"_
    - _"as a User i want to be able to edit any 1-rep max records i have entered in the event that i was bad at math at the time of recording"_

2. Stakeholders
    - _"As a Business owner, I want to be able to ** see who has signed up to use this app**, so that Track the apps success and growth"_
    - _"As a Business owner, I want to be able to know i have consent to access and use the data provided by users on sign up, so that I can optimise brand marketing"_
    - _"As a Business owner, I want to be able to know what movements are most popular, so that compare them with other movements and see why they are more popular with users"_
    - _"As a Business owner, I want to be able to promote my other products on this app seamlessly, so that I can optimise my brand marketing"_
    - _"As an Admin, I want to be able to Add new movements to the app, so that I don't have to ask the developer to do it every time we add a new movement"_
    - _"As an Admin, I want to be able to update movement video links, so that if/when they are re-filmed, i can update the app to show the newest content"_
    - _"As an Admin, I want to be able to Delete movements, so that if they become obsolete, or if i need to take them down, i can do so"_


#### __Project Goals__

> The Goal of this project is create a web application that enhances a user's physical fitness training through functional movement focused guidance and tracking of progress in addition to promoting elements of the client's business such as coaching, classes and community. 

#### __User Goals__

Based on user stories, user goals are defined as - _"create an app that..."_:
- _allows users to search and view specific functional training movements_
- _allows users to create, read, update, delete and track their development on specific goal-oriented movements_
- _allows users to keep track of movements they are focusing on developing, or keeping as a handy reference_
- _allows users to diversify their training with recommended alternatives_
- _allows users to record their own notes and data pertaining to a specific movement_
- _allows admins to see how many people use the app_
- _allows admins to create, read, update and delete content within the apps dataset_
- _allows admins to track the popularity of specific app content_


#### __Developer Goals__

- Create a an informative functional training tool
- push personal and professional capabilities as a full-stack software developer
- Create a web app that could potentially grow into a viable business opportunity in the future 
- fulfill all assessment and portfolio criteria


### **Scope Plane**

Based on the results of the strategy plane the following features have been focused on to develop:

1. **A role-based authentication-mitigated experience**
    - User's will be required to sign up and login to use the app
    - Admins will be able to access the admin panel with specific admin credentials

2. **a responsive search field that predicts what users are looking for, or lists search results based on entered criteria**
    - This will be housed in the Nav element of the app's html, as the search function should alwasy be accessible to authenticated users
    - the search field will generate real-time predictions based on the entered search criteria in a dropdown. selecting items from the dropdown will tae you directly to the movement, submitting criteria to the form will generate a list of possible results.

3. **An easily accessible menu where users can manage bookmarked/recorded data and their own user info**
    - off-canvas menu will be housed in the nav element of the page. When clicked, users will have immediate access to their bookmarked movements and their own profile data such as name and email address

4. **View selected movements**
    - based on the criteria given in the search, when a movement is selected, a movement video should be immediately displayed in addition to important key information relating to that movement

5. **Create, Read, Update, Delete specific user records pertaining to that movement**
    - within the view of the video and instructional content, record for the User's Latest One rep max for a weighted movement should be displayed. 
    - if the user has no records the field will give this feedback to the user
    - there will be buttons that will allow a user to add a new movement, or a button that will open an off-canvas element to edit or delete any of the recorded data.

6. **prompts**
    -  whenever a user performs any CRUD functionality on any dataset elements in the UI, the UI will generate a toast message to confirm the user has successfully carried out a function

7. **Bookmarking**
    - directly under the video, their will be a button that allows a user to bookmark a movement, which will then show up in their off-canvas menu.

8. **promote client brand**
    - the footer will contain links to socials, in addition to links to the Client's social media
    - the offcanvas menu will have a button that opens a new browser window where users can book classes


### **Structure Plane**
The App will use the Django web app framework to  extend specific HTML pages into a base template, then datasets from a hosted database will be rendered on html templates based on specific user and user interaction:

[ADD EDIT PROFILE FUNCTIONALITY THEN AMEND SITEMAP DIAGRAM AND THEN IMPLEMENT]


#### __Dataset Models | Database Tables__

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

#### **Wireframes**

Mobile View:

| Login Page | Sign-up Page | Sign-out Page |
|:-:|:-:|:-:|
| ![Login page](/static/media/readme-media/wireframes/mobile/11-log-in.webp) | ![Sign-up Page](/static/media/readme-media/wireframes/mobile/10-sign-up.webp) | ![Sign-out page](/static/media/readme-media/wireframes/mobile/12-sign-out.webp) |

| Index/dashbord | Navigation Menu | Navigation Menu Expanded |
|:-:|:-:|:-:|
| ![Dashboard page](/static/media/readme-media/wireframes/mobile/1-index-dashboard.webp) | ![Menu view](/static/media/readme-media/wireframes/mobile/2-menu-demo-1.webp) | ![Menu expanded](/static/media/readme-media/wireframes/mobile/3-menu-demo-2.webp) |

| Edit Profile Page | Edit Profile Page with edited fields | Search Results |
|:-:|:-:|:-:|
| ![Edit Profile Page](/static/media/readme-media/wireframes/mobile/8-edit-profile-1.webp) | ![Edit Profile edited view](/static/media/readme-media/wireframes/mobile/9-edit-profile-2.webp) | ![Search Results page](/static/media/readme-media/wireframes/mobile/4-search-results.webp) |

| Movement Detail Page | User 1-Rep-max records for that movement | add / edit a 1-rep max |
|:-:|:-:|:-:|
| ![Movement Detail page](/static/media/readme-media/wireframes/mobile/5-movement-detail.webp) | ![1-Rep-max records for that movement](/static/media/readme-media/wireframes/mobile/6-records-menu.webp) | ![add / edit a 1-rep max](/static/media/readme-media/wireframes/mobile/7-add-new-record.webp) |

Desktop / larger screen view:

| Dashboard/index | Navigation menu | Search Results Page |
|:-:|:-:|:-:|
| ![Dashbaord page Desktop](/static/media/readme-media/wireframes/desktop/01-dt-dashboard.webp) | ![Navigation menu desktop](/static/media/readme-media/wireframes/desktop/02-dt-menu.webp) | ![Search results page desktop](/static/media/readme-media/wireframes/desktop/03-dt-search-results.webp) |

| Dashboard/index | Navigation menu | Search Results Page |
|:-:|:-:|:-:|
| ![Movement details page desktop](/static/media/readme-media/wireframes/desktop/04-dt-movement-details.webp) | ![User 1-Rep-max records for that movement Desktop](/static/media/readme-media/wireframes/desktop/05-dt-1rm-records.webp) | ![edit/add 1rm desktop](/static/media/readme-media/wireframes/desktop/06-dt-1rm-form.webp) |


## Colour Scheme

As the branding and style is already created for the client, the Chrome extension [Site Palette](https://chrome.google.com/webstore/detail/site-palette/pekhihjiehdafocefoimckjpbkegknoh/related?hl=en-GB) was used to generate a board of colours to choose from when stylising the app elements:

![colour palette by Site Palette](/static/media/readme-media/colour-palette-1.png)

![colour palette by Site Palette](/static/media/readme-media/colour-palette-2.png)

As site palette only generated "like-colours" for the app, original brand colours have been placed below using a screenshot from [Colormind](http://colormind.io/template/material-dashboard/):

![Fly site Colours](/static/media/readme-media/fly-site-colours.png)

## Typography

According to Dev Tools, the Fly Site uses only a thin variation of the Montserrat font. As such, The montserrat font was imported from [Google Fonts](https://fonts.google.com/) to stay congruent with the business branding

![Montserrat Font: Google Fonts](/static/media/readme-media/montserrat-font-google.png)


## Imagery & Media

Imagery such as Logos were provided by the client. Access to the Client's Vimeo account to format the videos within Vimeo's API was also given. Slugs were then taken from vimeo and imported as keys within the database.
___

# F E A T U R E S

## Design Features

### **Front-End Mechanical Features**

**__Logging in__**

- when viewing the app a non-authenticated user, the app will alays redirect to the login screen, no matter that link is used to access the app.
- This is achieved by the use of class decorators within the views.py file, that generate that a user MUST be authenticated, else they are redirected to the login page.
- users can log in by providing a username and password
- Username and password are checked against the database by use of the Django Allauth plugin
- Incorrect username or password will just redirect to the login page
- correct details will redirect users to the dashboard of the app

**__Sign up__**
- Users can sign up if they do not have an account
- They can do so by clicking the link on the login page, which rediects to a sign up form
- the form requests the following fields be completed:
    - Username
    - Email Address
    - First Name
    - Last Name
    - Password
    - Password (again, for verification)
- failure to correctly enter all fields will result in a refresh of the page
- correctly submitting the form posts the data to the Database via use of the Allauth functions

**__Forgot password__**
- Users can reset their password by clicking on the "forgot password?" link on the login page, OR in the edit profile page
- the entering an email address emails a user with a reset password link. This is all handled by Django Allauth

**__Editing Personal Details__**
- When logged in, users can edit their first name and last name by selecting "Edit profile" from the navigaton menu
- Email change will be implemented in later iterations, as this will require some further security

**__Navigation Menu__**
- Once logged in, users can access the navigation menu by clicking the navigation button at the top left of the page
- when clicked, an off-canvas menu will appear, allowing users to:
    - Access a link that will always return the user to the dashboard
    - Access any movements a user has bookmarked 
    - Edit theiir profile
    - Sign out

**__Book Classes__**
- If authenticated, on the dashboard page, users can click a button that will redirect them to the booking system that the client uses to manage classes

**__Social features__**
- Links to social Media platforms for the business such as Instagram and Facebook appear as branded buttons at the bottom of the page in the footer.
- clicking on them will open the desired page in a seperate tab

**__Searching movements__**
- in the navbar, users can make use of the search field that allows them to search for specific movements
- when searching, the search criteria filters through objects in the "Movement" database to find objects contain any string values entered into the search field, for example, the terms "floor" or "press" would both return the movement "floor press" along with any other movements that contain those string values in their names
- on the search results page, users can click one of the results and will be redirected to the movement detail page for that movement

**__Movement Details__**
- when a moevement is selected, the database is queied and provides the following elements to the page:
    - A demonstration video of the moevement
    - Key information about the movement
    - The 1-rep Max records for that moevement by the specific authenticated user

**__Adding a 1-rep max__**
- Authenticated users can click on a button that will open an off canvas element containing a form
- The form will allow users to enter an integer value and hit submit
- outside the field, a label will indicate that this integer should represent Kilograms
- upon submitting, this integer is posted to the UserOneRepMax table, containing:
    - The integer value entered
    - The date it was recorded
    - What movement it was for
    - What user created the record

**__Viewing 1-rep maxes__**
- Authenticated users; when viewing a movement, will be shown their most recent 1 rep max directly below the video
- there is also a button that users can click, which will open an offcanvas element, displaying all of their previious 1-rep-max records

**__Editing/Deleting 1-rep maxes__**
- When viewing the offcanvas menu mentioned above, there are buttons which allow a user to edit the specific 1-rep-max record
    - This re-opens the form for adding a 1-re max in the offcanvas, but this time the target is that specific record
    - when submitted, the change is updated on the database
- The delete button is right next to the edit button, which; when clicked, removes the record


## Visual Features

## Data Management

All Data for this project is stored on a hosted server by ElephantSQL and Amazon Web Services on a TinyTurtle Package. The server is located in Ireland and is maintined by ElephantSQL.

### **Database Models/Structure**

The database contains the following tables:

**Movements**
- Houses all of the movements in the movement library
- contains the unique vimeo slug for each video, which calls the video from the vimeo database
- a unique slug field for the app, that identifies the movement for the brower
- a name field to identify the omvement to the user at the front end 

**Tags**
- contains a list of common tags associated with moevements in the library
- these tags are linked in each record by a foreign key, linking to the Movement Table
- Each tag has a boolean value of true or false, true meaning that the tag is associated with that specific movement
- This table was implemented with the hopes of adding more advanced search functionality, but due to setbacks in this iteration, this feature was postponed

**User Movement Notes**
- Contains a record of a User's Id as a foreign key, an associated movement as a foreign key and a notes field as a text field
- The Idea for this table is that a user can have a single record for each movement. a notes field which can be viewed and edited
- This table was implemented with the hopes of adding such a feature, but there was insufficient time available to implement during this iteration of the Project

**User Non-Auth Fields**
- This Table was to act as an extension of the User Table implemented by Allauth
- It contains non-sensetive user information such as:
    - a boolean value to check if users agree toa privacy policy/GDPR
        - As this project will not be published commercially at the time of submission/examination, this feature has not been implemented on the front end of the app
    - The last movement a user viewed
        - Due to time onstraints, this feature was not implemented in the first iteration of the project
- The fields would be indexed by a foreign key linking to the User table

**User One-Rep Maxes**
- This table indexes and cross references with 2 foreign keys from the following tables:
    - User
    - Movement
- it contains the following additional fields
    - Integer Field: for recording a 1-rep max (in Kilograms)
    - Date/Time field: Automatically fills when a form is submitted on the front end
- This table allows users to record accurate results, track their progress, and help manage the optimum working weight of their workouts

## 404 / 500 Features

## Agile Development Plan

First Iteration testing and feedback:

To simulate Agile principles, this project took an incremental review approach to project development, where the project was released in a beta version to the same group over 2 iterations. This allowed to get feedback on functions and basic developed elements and allowed for the project to adapt to the client's needs

New user stories:
- _"As a user, i would like to log out from the profile view page, as i would find this more intuitive."_
- _"As a user, i would like to have my personal settings be more visibly accessible so i can navigate the app more intuitively"_
- _"As a user, i would like to access the full list of movements in the library in addition to searching for them"_
- _"As a user, i would like to have a timer on the movement page, so i can track workout time, or rest periods when conducting a movement"_
- _"As a user, i would like to have a playlist of videos that iterates through my bookmarked movements for a streamlined workout"_
- _"As a user, i would like to access some of the partner app features on this app for a more seamless experience"_
- _"As a user, i would like to view the last movement i logged a 1-rep max on from the dashboard"_
- _"As a user, i would like to view my most viewed movement on the dashboard, as i keep searching for it"_

additional feedback:
- _"Users found the app to look quite empty"_
    - As the app's first iteration was to focus on Assessment criteria, second stage development will aim to pad out the user experience
- _"too many clicks to access a specific movement"_
    - aim to reduce number of clicks it takes a user to access a movement
- _"the green background does not sit well behind the objects"_
    - will remove for next iteration
- _"site elements seem a bit static and flat"_
    - objects will be assigned some javascript/css animation to give the objects more context


## Future Development

The following features were not implemented in this iteration of the project due to time constraints. But will be reviewed with the next iteration of the Project after this Project has been assessed:

1. Adding of User Notes on a movement
2. Implementation of a Terms/End User License agreement/GDPR disclaimer
3. Reactive Search field that responds in real-time to the users entered data
    - able to bypass search results page upon selecting a movement from a provided datalist depending on values keyed into search field
4. Remove the reloading of Page elements on submission/POST requests by utilizing async functions and fetch commmands in Javascript
5. Add the feature of allowing users to append notes to movements
6. Implement a secure automated method where users can request to change their email
7. Implement a feature that allows user's to Delete their account
8. Add a modal that asks the user to confirm deletion of a 1-rep max record upon selecting the delete button for a 1-rep max instead of just immediately deleting the item

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
- when a 1rm is entered, movement becomes un-bookmarked:
    - closing tag for the edit 1rm form was placed incorrectly inside a for loop on the template. replaced outside of loop and resolved issue

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
- connection refused (error: 111) when trying to reset password.
- use of brackets in search terms will yield no result.
- background of footer cant be made transparent

___

# T E C H N O L O G I E S

## Languages
- [Python 3.11.4](https://www.python.org/)
- [Javascript 5](https://en.wikipedia.org/wiki/JavaScript)
- [CSS 3](https://en.wikipedia.org/wiki/CSS)
- [HTML 5](https://en.wikipedia.org/wiki/HTML)

## Frameworks
- [Django 4.0](https://www.djangoproject.com/)
    - [Summernote](https://pypi.org/project/django-summernote/)
    - [Allauth](https://django-allauth.readthedocs.io/en/latest/)
    - [Gunicorn](https://gunicorn.org/)
- [Cloudinary](https://cloudinary.com/)

## Libraries
- [Bootstrap 5.3x](https://getbootstrap.com/)
- [Jquery 3.7.0](https://jquery.com/download/)

## Programs
- [VS Code](https://code.visualstudio.com/)
- [MS Powerpoint](https://www.microsoft.com/en-gb/)
- [MS Word](https://www.microsoft.com/en-gb/)
- [Google Chrome](https://www.google.com/intl/en_uk/chrome/)
    - Desktop
        - [Site Palette Extension](https://chrome.google.com/webstore/detail/site-palette/pekhihjiehdafocefoimckjpbkegknoh/related?hl=en-GB)
        - Devtools
    - Mobile
- [Mozilla Firefox](https://www.mozilla.org/en-GB/firefox/)
- [Safari](https://www.apple.com/uk/safari/)
- [Opera GX](https://www.opera.com/)
- [GIMP 2.10.32](https://www.gimp.org/)

## Web Applications / Services
- [Monday.com](https://monday.com/)
- [Github](https://github.com/)
- [Gitpod](https://gitpod.io/workspaces)
- [Colormind](http://colormind.io/template/paper-dashboard/)
- [Vimeo](https://vimeo.com/)
- [Youtube](https://www.youtube.com/)
- [Heroku](https://id.heroku.com/)
- [Elephant SQL](https://www.elephantsql.com/)
- [Chat GPT](https://openai.com/blog/chatgpt)
- [Zoom](https://zoom.us/)
- [Cloud Convert](https://cloudconvert.com/)

___

# T E S T I N G

Full Manual Testing of elements can be found in the appended document:

First Iteration testing and feedback:

To simulate Agile principles, this project took an incremental review approach to project development, where the project was released in a beta version to the same group over 2 iterations. This allowed to get feedback on functions and basic developed elements and allowed for the project to adapt to the client's needs

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

