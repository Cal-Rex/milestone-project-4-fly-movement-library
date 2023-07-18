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
| ![forms.py](/readme-media/testing/python-validation/forms-py.png) | ![models.py](/readme-media/testing/python-validation/models-py.png) | [settings.py](/readme-media/testing/python-validation/settings-py.png) ||
____

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
- js throws error in console when it has no message box to close, but doesnt impact site function.

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


