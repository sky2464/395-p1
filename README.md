# 395-p1
CSCI 395 - Project 1
To-Do App – CSCI 39548
Goals:
● Get you up-to-speed with very basic web programming, things like:
○ basic web framework to build a web application
○ basic html
○ basic http
○ basic sql using sqlite
○ basic session and cookies
Assignment:
● Create a (clunky) to-do list web app (website) that can:
○ Create a new user
○ Log in as a user (no password required, just have someone type in their name)
○ Be able to see and interact with their to-do items
■ Create new item(s)
■ See their item(s)
■ Mark item(s) as done
■ Delete item(s) altogether
○ IMPORTANT: the data should be persistent, if I restart your app, the data should
still be there
○ Log out
Requirements:
● Source code on your Github account
● A script in your Github repo called start.sh which will start your application and check for
dependencies (to grade, I am literally going to clone the master branch of your repo and
try running that script)
● Your script MUST work on a UNIX-based machine (Mac or Linux distro). If you have a
windows machine, please use software like VirtualBox or install a dual boot.
● Use either Flask (python), which we will support and cover in class, or Express (node.js),
which you would need to self-teach
● Use SQLite
NOT Required:
● Does NOT need to be a single page app. You are actually strongly encouraged to build
a clunky, multi-page application (think old internet websites)
● Does NOT need to be beautiful (good old fashioned html is fine, no need for any fancy
CSS or JS)
