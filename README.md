# 261P-FRQ-Autograder
Based on https://github.com/kb22/ML-React-App-Template.

Setting up the UI and Flask server
-----------------------
**Commands were run on Windows/Linux. Mac may have slightly different commands.**

If Python or npm are not present on the machine, they should also be installed first (using sudo or pip).

Setting up the interface:
1. Open up Powershell (or Command Prompt)
2. Navigate to the ui folder of the code
3. `npm install`
4. `npm start`

This starts running the UI which can be accessed at localhost:3000.
___
Setting up the Flask app:
1. Open up a second Powershell (or Command Prompt)
2. Navigate to the service folder
3. Make sure app.py is part of your FLASK_APP environment variable. This can be done by editing system environment variables directly, or using `set FLASK_APP=app.py`
4. `flask run`

This starts the flask app which receives requests and returns responses.

What the prototype does
------------------------
Enter a set of keywords, comma separated, into the keyword field, and those keywords will be compared with the text of the student field.

You can also enter synonyms for words, space separated. For example, with the keywords `blue aqua, red ruby`, the student text `the sky is blue, roses are ruby` would still be considered fully correct.

When "Score" is clicked, the app sends request to the Flask server at `/prediction`. The endpoint just does string compare, prints the keywords found, and the percentage of keywords found.

This functionality should be very different in the final product, but it is a framework for the UI and structure.

Various issues that may arise while trying to run or compile:
------------------------
`Commands or modules not found` (usually means system is lacking dependencies that need to be installed):

Try `pip install -r requirements.txt`

or
```
sudo apt install python3-flask
pip install flask_restplus
flask run
```
___
`Cannot import name 'cached_property' from 'werkzeug'`

Go to the file `fields.py` in your `flask_restplus` folder, and change the following line:

`from werkzeug import cached_property`
to
`from werkzeug.utils import cached_property`
___
You may want to run using a virtual environment:
```
virtualenv -p Python3
Scripts\activate.bat
flask run
```
