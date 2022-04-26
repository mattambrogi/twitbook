# twitbook

## What is it
Twitbook is a Twiiter-like app built with Django. This app is live at https://ma-twitbook.herokuapp.com/. Feel free to make an account and add some write some Tweets!

## Why I built it
Having just learned Django at the beginnging of 2021, I wanted to build something more complex to master CRUD aspects of the framework. A twitter like platform seemed like a perfect challenge and I was excited to figure out things like a following system and user profiles.

## Features
As a user of that app, I can
- Create an account
- Create posts
- Have a profile in which my bio and posts are displayed 
- Edit my profile bio
- View a list of all users and follow / unfollow others
- View a feed of all posts from people I follow
- Comment on posts
- Edit and delete posts that I created
- Delete comments that I created


## Technologies
- Django
- HTML, CSS, Bootstrap
- PostgreSQL
- Deployed on Heroku

## Technical challenges
- Implementing a follower system
- Displaying data from multiple database models within a single Django class based view (i.e. profile pulls info from User and Post models).
- Implementing custom template tags
  - Example: template tag which is used to make sure the feed only displays posts from people the user follows.


