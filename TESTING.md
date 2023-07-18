# F L Y - M O V E M E N T - L I B R A R Y
## M A N U A L - T E S T I N G

# Contents

- User Stories
    - User Stories: Answered
    - Project Goals: Achieved
- Manual Testing
    1. 404 / 500
    2. Login page
    3. Sign up page
    4. Forgot password
    5. Index
    6. Edit Profile
    7. Log out
    8. Search results
    9. Library
    10. movement details
____

## User stories Achieved:

- _"as a User i want to be able to edit any 1-rep max records i have entered in the event that i was bad at math at the time of recording"_
    - users can edit any one rep max for any movement they onter on the specific movement page, clicking th icon. then selecting the record from the list in the presented offcanvas. when they click the edit icon next to the record, they can then edit the record y filling in the form.

- _"As a user, i want to be able to log in so that i can view specific workout/movement tutorials"_
    - Log in feature enabled through django Allauth Plugin

- _"As a user, I want to be able to search for specific workouts, so that I can easily find the movement I am looking for"_
    - There is a search function which also has a responsive list generated in real time depending what is put into the fields
    - while the tage model is implemented in the app it is not utilised in this version

- _"As a User, I want to be able to Bookmark movements, so that I can refer to them easily at a later date"_
    - The bookmarking feature is available on every movement
    - A users bookmarks are always accessible from the bottom right of the app at any time when logged in

- ~_"As a User, I want to be able to know what other exercises compliment the ones i have bookmarked, so that I can expand my training"_~
    - not implemented in this version due to time constraints

- ~_"As a User, I want to be able to create my own flow of movements, so that i can keep myself right during my own training"_~
    - Clarified with team at start of project this would not be iable in this iteration

- _"As a User, i want to be able to search for movements even if i am unsure of their names so that I can find my moevements easily without having to know all the correct terminology"_
    - search function slices and maps words with javascript, meaning it will search every word of every movement for any combination of strings. maximising search capability
    - this will be further enhanced in future iterations with the implementation of the tags table

- ~_"As a user, I want to be able to have recommendations from my searches, so that if I cant find the movement I am looking for, I have alternatives to try"_~
    - not implemented in this iteration

- ~_"As a User i want to be able to add my own personal notes to a movement, for my own reference so that i can keep track of different aspects of my workout and training"_~
    - removed from iteration due to time constraints

- _"As a User I want to be able to record my own 1-rep maxes in the app and date them so that I can track my progression"_
    - Users can record their one rep max for any movement
    - whenever a record is creted, the date is automatically saved with the record at the time of creation

- ~_"as a User I want to be able to edit any notes I attach to a workout so that I can amend my notes to have relevant information when I am training"_~
    - not implemented in this iteration due to time constraints

- ~_"As a user, i would like to log out from the profile view page, as i would find this more intuitive."_~
    - ran out of time to implement, log out feature still omre readily available from dashboard

- _"As a user, i would like to have my personal settings be more visibly accessible so i can navigate the app more intuitively"_
    - settings removed from dropdowna nd given dedicated offcanvas on same level as dashboard commands

- _"As a user, i would like to access the full list of movements in the library in addition to searching for them"_
    - a panel on the dashboard is available that takes you to a full list of movements to select from

- ~_"As a user, i would like to have a timer on the movement page, so i can track workout time, or rest periods when conducting a movement"_~
     - agreed not to be implemented in this iteration

- ~_"As a user, i would like to have a playlist of videos that iterates through my bookmarked movements for a streamlined workout"_~
    - not implemented in this iteration

- _"As a user, i would like to access some of the partner app features on this app for a more seamless experience"_
    - links that open to the gyms booking page given an integral panel on the dashboard

- _"As a user, i would like to view the last movement i logged a 1-rep max on from the dashboard"_
    - panel available on dash that shows thumbnail of movement in additon to acting as a link ot go straight to that movement

- ~_"As a user, i would like to view my most viewed movement on the dashboard, as i keep searching for it"_~
    - not implemented due to time constraints


## User Goals achieved:

- _allows users to search and view specific functional training movements_
    - yes, with search function and movement details view

- _allows users to create, read, update, delete and track their development on specific goal-oriented movements_
    - yes, one rep max feature allows users to create, read, update and delete important tracking info for lifting

- _allows users to keep track of movements they are focusing on developing, or keeping as a handy reference_
    - bookmarks feature allows movements to be readily avialable to users

- ~_allows users to diversify their training with recommended alternatives_~
    - not implemented in this version

- ~_allows users to record their own notes and data pertaining to a specific movement_~
    - not implemented in this version

- _allows admins to see how many people use the app_
    - features supplied by django

- _allows admins to create, read, update and delete content within the apps dataset_
    - features supplied by django

- _allows admins to track the popularity of specific app content_
    - features indirectly supplied by django

- ~_allows users to use the app as a guide through their workout_~
    - no features to support goal implemented in this version

## **Automated Testing**

### **Accessibility**

Lighthouse in devtools on chrome was used to establish appropriate accessibility and best practices:

| sign in | sign out | sign up |
| :-----: | :------: | :-----: |
| ![Lighthouse sign in](/readme-media/testing/lighthouse/sign-in.png) | ![Lighthouse sign out](/readme-media/testing/lighthouse/sign-out.png) | ![Lighthouse sign up](/readme-media/testing/lighthouse/sign-up.png) |

| Password Reset | Search Results | Library |
| :-----: | :------: | :-----: |
| ![Lighthouse Password Reset](/readme-media/testing/lighthouse/password-reset.png) | ![Lighthouse Search Results](/readme-media/testing/lighthouse/search-results.png) | ![Lighthouse Library](/readme-media/testing/lighthouse/library.png) |

| Edit Profile | Movement | Index |
| :-----: | :------: | :-----: |
| ![Lighthouse Edit Profile](/readme-media/testing/lighthouse/edit-profile.png) | ![Lighthouse Movement](/readme-media/testing/lighthouse/movement.png) | ![Lighthouse Index](/readme-media/testing/lighthouse/) |



## **Code Validattion**

### __HTML__

[W3 Validator](https://validator.w3.org/) was used to check the HTML of all Pages cuctomised/not autocreated by django.

**index**

[Click to view index.html validation](/readme-media/testing/html-validation/index.png)

**library**

[Click to view library.html validation](/readme-media/testing/html-validation/library.png)

**login**

[Click to View accounts/login.html validation](/readme-media/testing/html-validation/login.png)

**Movement**

[Click to View movement.html validation](/readme-media/testing/html-validation/movement.png)

**Password-reset**

[Click to View accounts/password_reset.html](/readme-media/testing/html-validation/password-reset.png)

**Search results**

[Click to View search_results.html](/readme-media/testing/html-validation/search-results.png)

**Sign up**

[Click to view accounts/signup.html](/readme-media/testing/html-validation/signup.png)


### __CSS__

[Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check the CSS of all Stylesheets:

**Account pages specific styling**
[Click to view account-style.css](/readme-media/testing/css-validation/account-style-css.png)

**Library and search result specific styling**
[Click to view library.css](/readme-media/testing/css-validation/library-css.png)

**style.css**

[Click here to view style.css](/readme-media/testing/css-validation/)


#### __javascript__

[JSHint](https://jshint.com/) was used to validate all of the javascript files for this project:

**auth template specific JS**
[Click to view auth-styling.js](/readme-media/testing/js-validation/auth-styling-js.png)

**search function js**
[Click to view js for search suggestions function](/readme-media/testing/js-validation/base-search-js.png)

**edit profile js**
[Click to view input field override js](/readme-media/testing/js-validation/edit-profile-js.png)

**Base JS for all docs**
[Click to view main JS file](/readme-media/testing/js-validation/fml-script-js.png)

**JS for movement template**
[Click to view JS specific to the movement template](/readme-media/testing/js-validation/movement-js.png)


#### __Python/Django__

All python/Django code was checked using the [CI Python Linter](https://pep8ci.herokuapp.com/)

| admin.py | FlyMovementLibrary/urls.py | movelibrary/urls.py |
|:-:|:-:|:-:|
| ![admin.py](/readme-media/testing/python-validation/admin-py.png) | ![FML/urls.py](/readme-media/testing/python-validation/fml-urls-py.png)| ![urls.py](/readme-media/testing/python-validation/urls-py.png) |

| forms.py | models.py | settings.py | views.py |
|:-:|:-:|:-:|:-:|
| ![forms.py](/readme-media/testing/python-validation/forms-py.png) | ![models.py](/readme-media/testing/python-validation/models-py.png) | ![settings.py](/readme-media/testing/python-validation/settings-py.png) | ![views.py](/readme-media/testing/python-validation/views-py.png) |

____


## Manual testing

1. 404/500

![404/500](/readme-media/testing/manual/404.gif)

working:
 + Return to dashboard works
 + page defaults to 404 if a page cant be found

bugs:
 - any slug outside a first tier 404 will not activate the 404/500 view. so bookmarks are unavailable on 404 page

___

2. Login page

![login page](/readme-media/testing/manual/login-page.gif)

Working:
+ forgot password link
+ sign up link
+ remember me button
+ sign in button

bugs:
- will generate 2 messages upon sign in if a user signs out and then back in again

___

3. Signup page

![sign up](/readme-media/testing/manual/Sign-up.gif)

Working:
+ all fields working
+ cannot use duplicate email addresses
+ link back to sign in
+ form works

Bugs: none

4.  Forgot Password

![Forgot password](/readme-media/testing/manual/forgot-password.gif)

Working:
+ buttons
+ input field
+ redirect on failure

bugs:
- email recovery not working because not implemented for assessment

5. Index

![index](/readme-media/testing/manual/index.gif)

Working:
+ search button animation on hover
+ search button opens search offcanvas on click
+ predictive/realtime search results (keyboard only)
+ li elements animate correctly on hover
+ search query loads into search page
+ last movement panel shows last movement viewed
+ predicted search suggestions take user  straight to movement
+ last recorded 1-rep max panel updates
+ nav buttons animate on hover
+ logo on top left returns to dashboard
+ all links in account offcanvas working
+ full library link take to correct page

bugs:
- duplicate messages on sign in if user signs out and then back in

____


6. Edit Profile

![Edit Profile](/readme-media/testing/manual/edit-profile.gif)

Working:
+ input fields
+ post method to update fields
+ message to confirm update
+ offcanvas functions provided by base html
+ buttons animate on hover

Bugs:
- search button animates on form button hover

____

7. log out

![log out](/readme-media/testing/manual/log-out.gif)

working:
+ return to dashboard button
+ log out button

bugs: none

____

8. search results

![Search results](/readme-media/testing/manual/search-results.gif)

working:
+ list items animate on hover
+ base html functions like off canvas menus working
+ nav buttons hover
+ search function works within search function

bugs:
- none that havent already been mentioned

___

9. Library Page

![library](/readme-media/testing/manual/library.gif)

Working:
+ every list item animates on hover
+ every list item takes you to the correct movement and loads correctly
+ All base html templae functions work

bugs: none

____

10. Movement details

![movement-details](/readme-media/testing/manual/movement-details.gif)

working:
+ specific directions for movement available.
+ link to full library available
Search function works same as all other templates
+ video loads correctly
+ bookmark feature works
+ add new one rep max works
+ conditional statement of add 1rm changed with value upon database containing a record. will revert back when there is no record
+ user can add a new value
+ user can update a value
+ user can delete a value
+user can list full record of all recorded data

bugs:
- search offcanvas does not have scroll ability


