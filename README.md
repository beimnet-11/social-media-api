# Social Media API

## Author
Beimnet Abera
ALX Backend Capstone Project


## Description
This project is a complete social media backend API built with Django and Django REST Framework. The API features user authentication, post management, likes, comments, and role-based access control. Users can create posts, like/unlike content, and comment on posts with proper authorization.


## Features

### Authentication

User registration with email and username
User login with token-based authentication
Secure password handling



### Posts

Users can create, read, update, and delete their own posts
Users can view all posts in the platform
Partial updates supported via PATCH method


### Authorization
Users can only edit or delete their own posts
Authentication required for all actions except registration
Proper permission checks for all operations


## API Endpoints

### Authentication
POST /api/user/register/ - Register new user


http://127.0.0.1:8000/api/user/register/
{
  "username": "15beimnet",
  "email": "15beimnet@example.com",
  "password": "15securepassword123",
  "password2": "15securepassword123"
}
POST /api/user/login/ - Login user and get token

 http://127.0.0.1:8000/api/user/login/
{
  "username": "15beimnet",
  "password": "15securepassword123",
  "password2": "15securepassword123"
}

token: 5f7d07f287e78abe8f734eb8c4a1b6bcd89716e0
Content-Type     application/json
Authorization    Token f7d07f287e78abe8f734eb8c4a1b6bcd89716e0


### POSTS
GET /api/posts/ - Get all posts
POST /api/posts/ - Create new post
GET /api/posts/{id}/ - Get specific post
PUT /api/posts/{id}/ - Update post
PATCH /api/posts/{id}/ - Partial update post
DELETE /api/posts/{id}/ - Delete post

 http://127.0.0.1:8000/api/posts/

{
"content": "Testing my ALX capstone API - post creation working! "
}



