# This is a resume website created using flask app.
User can choose the language, the color and the font of the website.

There is more to offer...

## The first way to run it: flask run
```
flask run
```
You may need to set up the environment variable so that flask knows where to look for the py file:
For windows:
```
set FLASK_ENV=development
```
In this way the last line of the code will be ignored.
## The second way to do that
```
python app.py
```
For this error:

ModuleNotFoundError: No module named 'werkzeug.contrib'

Try the following solutions:
```
pip3 uninstall Werkzeug
pip3 install Werkzeug==0.16.0
```
