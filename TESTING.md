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
    - Log out
    - Search results
    - Library
    - movement details


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

6. 
