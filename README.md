# twitbook
A Twiiter-esk app built with Django.

This app is deployed at https://ma-twitbook.herokuapp.com/

As a user of that app, one can
- Create an account
- Create posts
- Have a profile in which their bio and posts are displayed 
- Edit the info within their profile
- View a list of all users and follow / unfollow others
- View a feed of posts from people they follow, much like a twitter feed
- Comment on posts
- Edit and delete posts (that they created)
- Delete comments (that they created)



The front-end was styled using Bootstrap. But the focus of this project was the backend.

Particularly interesting challenges were
- Implementing a follower system
- Learning to display info from a variety of different Django models within one class based view within a monolithic Django project. I.e. the profile pulls info from the user model and post model.
