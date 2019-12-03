# flask-restful-blueprint-mongo-setup
flask-restful,flask-blueprint,mongo db,set up and project directory structure example

app/__init__.py 

This file define the create_app() function 
here do the following 
1. connect mongo DB 
2. register all blueprint into the Flask app 
3. then lastly return back the app object to be used in run.py 


run.py 

this is the point for Flask run 
1st import create app function for the file above 
then the app object here 
then the Flask app will start 

app/api.py 

this is the place the define the routes 

1.Blueprints - Break the whole flask app into different part of smaller app 
  - example , Api one part,admin one part,then we will have 2 blueprints 

2. Pass the Blueprint object into Api object(this from Flask-Restful)
    Api() object in Flask-Restful need the Flask App as a parameter.
    the a Blueprint is a "little Flask app"
    so we pass the Flask app into the `Api()`
    
3. we need to add `Resource` into the `Api()` object with the path you want to access it 
  Resource file is the file you define the [get,post,delete,path] when the traffic go to the `path` you set.
  
  
Resource folder 

All file inside this will be the Resource object which you define [GET,POST,UPDATE,DELETE] operation for each endpoint 
and use it to define the part and for `app/api.py` file above.

Database package 

This package is used to define all the Mongo DB models.

