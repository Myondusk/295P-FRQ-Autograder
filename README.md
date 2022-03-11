# 261P-FRQ-Autograder
Based on https://github.com/kb22/ML-React-App-Template.

Windows
-----------------------
Setting up the server:
1. Open up Command Prompt
2. Navigate to the ui folder
3. *npm install -g server*
4. *npm run build*
5. *npx serve -s build -l 3000*

This starts running the UI which can be accessed at localhost:3000.

Setting up the Flask app:
1. Open up a second Command Prompt
2. Navigate to the service folder
3. Set up a virtual environment to run. Skip to step 6 if not using a virtual environment.
4. *virtualenv -p Python3 .*
5. *Scripts\activate.bat*
6. Make sure app.py is part of your FLASK_APP environment variable. Otherwise use *set FLASK_APP=app.py*
7. *flask run*

This starts the flask app which receives requests and returns responses.
