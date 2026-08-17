# CodeAlpha_Social-Media-Platform


# SocialHub - Mini Social Media Platform

## Internship Task

**Program:** Artificial Intelligence Tasks & Instructions  
**Organization:** CodeAlpha  
**Task:** Task 2 - Social Media Platform  
**Project Type:** Full-Stack Web Application  
**Frontend:** HTML5, CSS3, JavaScript  
**Backend:** Django  
**Database:** SQLite  
**Programming Language:** Python  

---

## Project Overview

SocialHub is a modern mini social media web application developed using Python and Django.

The application allows users to create accounts, manage their profiles, create text and image-based posts, upload multiple images, like and comment on posts, follow other users, search for users, and view followers and following lists.

The project demonstrates practical implementation of Django authentication, database relationships, file uploads, AJAX interactions, responsive frontend design, and CRUD operations.

---

## Main Features

### 1. User Authentication

- User registration
- User login
- User logout
- Secure authentication using Django
- Login-protected pages and actions
- Session-based authentication

### 2. User Profiles

- Individual profile page for every user
- Username display
- Profile information
- Profile picture upload from local files
- Bio editing
- Edit profile functionality
- User post history
- Followers count
- Following count
- Total likes received

### 3. Profile Statistics

Each user profile displays professional statistics:

- Posts
- Followers
- Following
- Total Likes

Users can also open:

- Followers list
- Following list
- Other users' profiles

### 4. Post Management

Users can:

- Create posts
- Add text content
- Upload images from local files
- Upload multiple images in one post
- Preview selected images
- View posts in the home feed
- Delete their own posts

Posts contain:

- Author information
- Post content
- Uploaded images
- Like count
- Comment count
- Comments
- Creation time

### 5. Like System

The application provides a complete like system.

- Like posts
- Unlike posts
- One user can like a post only once
- Like count updates dynamically
- Database prevents duplicate likes
- AJAX-based like interaction
- Page does not jump to the top after liking

### 6. Comment System

Users can interact with posts through comments.

- Add comments
- Multiple comments on the same post
- Display comment author
- Display comment content
- Display comment time
- AJAX-based comment submission
- Page position remains unchanged after commenting

### 7. Follow System

Users can connect with other users.

- Follow users
- Unfollow users
- Prevent self-following
- Prevent duplicate follow relationships
- View followers
- View following users
- Open profiles from follower/following lists
- AJAX-based follow interaction

### 8. User Search

SocialHub includes a user search system.

Users can:

- Search for other accounts
- Search using username
- Search usernames with `@`
- Search usernames without `@`
- View matching accounts
- Open searched users' profiles

Example:

```text
@Mohan_Khadka12
@Mohan_Khadka12@
Mohan_Khadka12
````

The search system handles these username formats appropriately.

### 9. Multiple Image Posts

Users can upload multiple images to a single post.

Features include:

* Local file selection
* Multiple image selection
* Image preview
* Image gallery
* Django media file handling
* Separate storage for post images

### 10. Profile Picture

Users can upload their profile picture directly from their computer.

Supported through Django media uploads.

Profile pictures are stored inside:

```text
media/profile_pictures/
```

### 11. AJAX Interactions

AJAX / Fetch API is used for important interactions.

AJAX functionality includes:

* Like
* Comment
* Follow
* Unfollow

This improves the user experience because the complete page does not need to reload after every interaction.

### 12. Professional UI Design

SocialHub includes a responsive and modern interface.

The design contains:

* Modern navigation bar
* Search bar
* Profile cards
* Profile statistics
* Post cards
* Image galleries
* Like buttons
* Comment sections
* Follow buttons
* Followers page
* Following page
* Responsive layout
* Mobile-friendly design
* Clean typography
* Interactive buttons
* Smooth user interactions

---

## Project Structure


social_media/
│
├── manage.py
├── db.sqlite3
│
├── social_media/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── social/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_comment_options_alter_post_options_and_more.py
│   │   ├── 0003_like_alter_comment_options_alter_post_options_and_more.py
│   │   └── 0004_alter_postimage_options_and_more.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│   └── social/
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       ├── edit_profile.html
│       ├── create_post.html
│       ├── followers.html
│       ├── following.html
│       └── search.html
│
├── static/
│   └── social/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
│
├── media/
│   ├── post_images/
│   └── profile_pictures/
│
└── venv/
```

---

## Backend Architecture

The Django project follows a standard project and application structure.

### Project

```text
social_media/
```

The project contains:

* Settings
* Main URL configuration
* ASGI configuration
* WSGI configuration

### Application

```text
social/
```

The application contains:

* Models
* Views
* Forms
* URLs
* Admin configuration
* Tests
* Database migrations

---

## Database Models

SocialHub uses Django ORM and SQLite to manage application data.

### Profile Model

Stores additional information related to users.

Main fields:

* User
* Bio
* Profile picture
* Created date

### Post Model

Stores posts created by users.

Main fields:

* Author
* Content
* Created date
* Updated date

### PostImage Model

Stores images associated with posts.

Main fields:

* Post
* Image
* Created date

A single post can contain multiple images.

### Comment Model

Stores comments made by users.

Main fields:

* Post
* Author
* Text
* Created date

A post can contain multiple comments.

### Like Model

Stores likes made by users.

Main fields:

* Post
* User
* Created date

A unique database constraint prevents a user from liking the same post more than once.

### Follow Model

Stores follower and following relationships.

Main fields:

* Follower
* Following
* Created date

Database constraints prevent:

* Duplicate follow relationships
* Following yourself

---

## Database Relationships

User
 │
 ├── Profile
 │
 ├── Posts
 │    ├── Post Images
 │    ├── Likes
 │    └── Comments
 │
 └── Follow Relationships
      ├── Followers
      └── Following
```

---

## Technologies Used

| Technology       | Purpose                       |
| ---------------- | ----------------------------- |
| Python           | Backend programming           |
| Django           | Web framework                 |
| SQLite           | Database                      |
| HTML5            | Web page structure            |
| CSS3             | Styling and responsive design |
| JavaScript       | Frontend interactions         |
| AJAX / Fetch API | Dynamic interactions          |
| Pillow           | Image processing              |
| Django ORM       | Database management           |

---

## Installation

### Step 1 - Create Virtual Environment

```bash
python -m venv venv
```

### Step 2 - Activate Virtual Environment

For Linux:

```bash
source venv/bin/activate
```

### Step 3 - Install Django

```bash
python -m pip install django
```

### Step 4 - Install Pillow

```bash
python -m pip install Pillow
```

---

## Database Setup

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Check the Django project:

```bash
python manage.py check
```

Expected output:

```text
System check identified no issues (0 silenced).
```

---

## Run the Project

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## Admin Panel

SocialHub uses Django's built-in admin panel for managing application data.

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

---

## Application Workflow


User Registration
       │
       ▼
User Login
       │
       ▼
Home Feed
       │
       ├───────────────┐
       ▼               ▼
Create Post       Search Users
       │               │
       ▼               ▼
Upload Images     View Profile
       │               │
       ▼               ▼
Publish Post      Follow / Unfollow
       │               │
       ├───────┬───────┘
       ▼       ▼
     Like    Comment
       │       │
       └───┬───┘
           ▼
      Social Interaction
           │
           ▼
   Followers / Following
```

---

## Key Django Concepts Demonstrated

This project demonstrates practical knowledge of:

* Django project structure
* Django applications
* URL routing
* Function-based views
* Django models
* Django ORM
* ForeignKey relationships
* OneToOne relationships
* Database constraints
* Django forms
* User authentication
* Login-required views
* CSRF protection
* CRUD operations
* File uploads
* Media files
* Static files
* Django templates
* Template inheritance
* AJAX requests
* Fetch API
* Database migrations
* Admin panel
* Responsive frontend design

---

## Security and Validation

The project uses Django's built-in security and validation features.

Implemented security and validation include:

* CSRF protection
* User authentication
* Login-required views
* Form validation
* Database constraints
* Unique like validation
* Follow relationship validation
* Self-follow prevention
* Post ownership validation
* Protected user actions

---

## Media File Management

User-uploaded files are stored inside the media directory.

### Post Images

```text
media/post_images/
```

### Profile Pictures

```text
media/profile_pictures/
```

Django's media configuration is used to serve uploaded files during development.

---

## Static File Management

Frontend CSS and JavaScript files are stored inside:

```text
static/social/
```

CSS:

```text
static/social/css/style.css
```

JavaScript:

```text
static/social/js/script.js
```

---

## Responsive Design

The interface is designed to work across different screen sizes.

Supported layouts include:

* Desktop
* Laptop
* Tablet
* Mobile

The frontend uses responsive CSS techniques to provide a better user experience on different devices.

---

## User Experience

SocialHub focuses on providing a smooth and simple social media experience.

Important UX features include:

* No unnecessary page reloads for likes
* No unnecessary page reloads for comments
* No unnecessary page reloads for follow actions
* Image previews
* Easy profile navigation
* Search functionality
* Clear profile statistics
* Responsive design
* Simple navigation

---

## Project Goal

The main goal of this project is to build a functional mini social media platform using Django and demonstrate practical full-stack web development skills.

The project combines:

* Frontend development
* Backend development
* Database management
* Authentication
* File handling
* AJAX interactions
* User relationships
* Responsive UI design

---

## CodeAlpha Task Requirements

The project fulfills the main requirements of CodeAlpha Task 2:

### User Profiles

Implemented with:

* Profile pages
* Profile pictures
* Bio
* Profile statistics
* Edit profile functionality

### Posts and Comments

Implemented with:

* Text posts
* Multiple image uploads
* Post deletion
* Multiple comments
* Comment display

### Like and Follow System

Implemented with:

* Like / unlike
* One-like-per-user restriction
* Follow / unfollow
* Followers list
* Following list
* User profile navigation

### Frontend

Implemented using:

* HTML
* CSS
* JavaScript
* AJAX / Fetch API

### Backend

Implemented using:

* Python
* Django
* Django ORM

### Database

Implemented using:

* SQLite
* Django database models
* Relationships
* Constraints

---

## Testing

The project includes a Django test file:

```text
social/tests.py
```

The Django system check can be executed using:

```bash
python manage.py check
```

---

## Future Improvements

Possible future improvements include:

* Real-time notifications
* Direct messaging
* Story feature
* Post editing
* Hashtags
* Advanced search
* Image optimization
* Video posts
* Email verification
* Password reset
* REST API
* PostgreSQL database
* Cloud media storage
* Deployment to a production server

---

## Project Status

**Status:** Completed

**Task:** CodeAlpha Task 2 - Social Media Platform

**Application:** SocialHub

**Backend:** Django

**Frontend:** HTML, CSS, JavaScript

**Database:** SQLite

---

## Conclusion

SocialHub is a functional and professional mini social media platform built with Python and Django.

The application provides user authentication, profile management, post creation, multiple image uploads, likes, comments, follow and unfollow functionality, user search, followers and following management, AJAX interactions, media file handling, and responsive UI design.

This project demonstrates practical experience in full-stack web application development and covers the major requirements of the CodeAlpha Social Media Platform task.



```
```
