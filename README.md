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

User Details table model:
|     id     | first_name | last_name | username    | password  |   email    | T_and_Cs |
| ---------- | ---------- | --------- | ----------- | --------- | ---------- | -------- |
| PrimaryKey | CharField  | CharField | CharField   | TextField |    email   | Boolean  |
|     1      | Andy       | Roux      | exampleUser | Guest+1   | e@mail.com | True     |

MovementLibrary Table:
|     id     | movement_name |   vid_link    |       tags        |
| ---------- | ------------- | ------------- | ----------------- |
| PrimaryKey |   TextField   |   TextField   |       [list]      |
|     1      |  Split Squat  | x.youtube.com | [lower, strength] |

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

### **Skeleton Plane**

## Colour Scheme

## Typography

## Imagery & Media
___