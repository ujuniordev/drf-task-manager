# Task Manager - API
## Project Portfolio 5

[Frontend: Link to the deployed Heroku app](https://task-manager-pp5.herokuapp.com/)

[Frontend: Link to the GitHub repository](https://github.com/ujuniordev/task-manager-pp5/)

[Backend: Link to the deployed Heroku app](https://drf-task-manager.herokuapp.com/)

[Backend: Link to the GitHub repository](https://github.com/ujuniordev/drf-task-manager/)

## Modules
- asgiref==3.6.0
- cloudinary==1.32.0
- dj-database-url==0.5.0
- dj-rest-auth==2.1.9
- Django==3.2.18
- django-allauth==0.44.0
- django-cloudinary-storage==0.3.0
- django-cors-headers==3.14.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.2.2
- gunicorn==20.1.0
- oauthlib==3.2.2
- Pillow==9.5.0
- psycopg2==2.9.6
- PyJWT==2.6.0
- python3-openid==3.2.0
- pytz==2023.3
- requests-oauthlib==1.3.1

## Libraries
- Django Cloudinary Storage
- Pillow (image processing capabilities)
- Django Rest Auth
- PostgreSQL
- Cors Headers

## Frameworks
- Django REST Framework

## Platforms
- Cloudinary - Storage of image files
- Github - Repository with Git version control
- GitPod - IDE used for development
- Heroku - Hosting of DRF database (until November 2022)
- ElephantSQL - Hosting of DRF database (from November 2022)

# Testing
## Task Management Functionality:

1.  **Add Task:**
    
    -   Click on the "Add Task" button or link.
    -   Fill in the task title and description.
    -   Click the "Save" button.
    -   Verify that the task appears in the task list with the correct details.
    -   PASS

2.  **Edit Task:**
    
    -   Click on an existing task to open the task details.
    -   Click on the "Edit" button.
    -   Modify the task's title and/or description.
    -   Click the "Save" button.
    -   Verify that the task details have been updated accordingly.
    -   PASS

3.  **Delete Task:**
    
    -   Click on an existing task to open the task details.
    -   Click on the "Delete" button.
    -   Verify that the task has been removed from the task list.
    -   PASS

## User Authentication:

4.  **User Registration:**
    
    -   Navigate to the registration page.
    -   Fill in the registration form with a valid username and password.
    -   Click the "Sign Up" button.
    -   Verify that a new account is created, and the user is redirected to the login page.
    -   PASS

5.  **User Login:**
    
    -   Navigate to the login page.
    -   Enter the username and password of an existing account.
    -   Click the "Sign In" button.
    -   Verify that the user is successfully logged in and can access their tasks.
    -   PASS

6.  **Invalid Login Attempt:**
    
    -   Navigate to the login page.
    -   Enter an incorrect username or password.
    -   Click the "Sign In" button.
    -   Verify that the application displays an error message indicating invalid credentials.
    -   PASS

## Deployment

### Local Deployment

The code for this project was written using the Gitpod IDE. To preview the project in the development environment, follow these steps:

1.  In your terminal within the Gitpod IDE, run the following command:
        
    `python3 manage.py runserver` 
    
    This will start the Django development server and open port 8000.
    
2.  When a popup window appears, click "Open Browser" to view your project in your web browser.
    

To create a local copy of this repository, you can clone the project using the following command in your IDE's terminal:

`git clone https://github.com/ujuniordev/drf-task-manager.git` 

Alternatively, if you're using Gitpod, you can click the link below to create your own workspace using this repository. This will set up a development environment for you to work on the project.

[![Open in Gitpod](https://camo.githubusercontent.com/76e60919474807718793857d8eb615e7a50b18b04050577e5a35c19421f260a3/68747470733a2f2f676974706f642e696f2f627574746f6e2f6f70656e2d696e2d676974706f642e737667)](https://gitpod.io/#https://github.com/ujuniordev/drf-task-manager)

### Preparing File for Deployment


If you haven't already configured Postgres for use in your deployed application, please follow these steps:

1.  Open your terminal and enter the following command to install the psycopg2-binary package:
    
    `pip3 install psycopg2-binary` 
    
2.  Install Gunicorn, which will act as your web server, with the following command:
    
    `pip3 install gunicorn` 
    
3.  If you have not yet created a requirements.txt file or if you've added new packages to your project, update the requirements.txt file by running the following command:
    
    `pip3 freeze --local > requirements.txt` 
    
    This command will generate or update a file named requirements.txt, which contains a list of all the packages that Heroku will need to install to run your application.
    
4.  Create a Procfile in the root folder of your project. Inside the Procfile, add the following line:
    
    `web: gunicorn <app_name>.wsgi:application` 
    
    Make sure to replace `<app_name>` with the actual name of your Django application. This Procfile tells Heroku to use Gunicorn to serve your Django application.
    
Once you've completed these steps, your project should be better prepared for deployment, especially when using Heroku or a similar platform.

### ElephantSQL Deployment


To host your database using ElephantSQL and integrate it into your project, follow these steps:

1.  **Create an ElephantSQL Account:**
    
    -   Visit the provided [link](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up) for instructions on creating an ElephantSQL account if you haven't already.
2.  **Log in to ElephantSQL Dashboard:**
    
    -   Log in to your ElephantSQL account to access the dashboard.
3.  **Create a New Instance:**
    
    -   In the ElephantSQL dashboard, click on "Create New Instance."
4.  **Configure Your Instance:**
    
    -   Give your plan a name, typically using the name of your project.
    -   Select the "Tiny Turtle (Free)" plan.
    -   Leave the "Tags" field blank.
    -   Click "Select Region" and choose a data center location near you.
    -   Click "Review," and if everything looks correct, click "Create Instance."
5.  **Copy the Database URL:**
    
    -   Go back to your ElephantSQL dashboard and click on the name of your project.
    -   Copy the database URL for your project.
6.  **Update Your Project Configuration:**
    
    -   In your project's `env.py` file (create it if it doesn't exist), create a new key called `DATABASE_URL` and set its value to the ElephantSQL database URL you copied, like this:
                
       `os.environ.setdefault("DATABASE_URL", "my_copied_database_url")` 
        
    -   Make sure to import the `os` module and check if the `env.py` file exists at the top of your `settings.py` file:
                
    `import os 
    
    if os.path.isfile("env.py"):
        import env` 
        
    -   Replace the database URL in your project's `settings.py` with the following code to fetch the value from the environment variables:        
        `os.environ.get("DATABASE_URL")` 
        
7.  **Configure Heroku:**
    
    -   Paste the database URL into the config vars section of your project on Heroku. You'll find this in the "Settings" section of your Heroku app.
8.  **Install `dj-database-url` Package:**
    
    -   In your terminal, run the following command to install the `dj-database-url` package, which will help you configure your database URL:
                
        `pip3 install dj-database-url` 
        
9.  **Update `requirements.txt`:**
    
    -   After configuring the database URL, update your project's `requirements.txt` file by running the following command:
                
        `pip3 freeze --local > requirements.txt` 
        
With these steps completed, your project should be configured to use the ElephantSQL database, both locally and when deployed on Heroku. Make sure to test your application to ensure that it's connecting to the database as expected.

### Heroku Deployment

This project utilizes [Heroku](https://www.heroku.com/), a Platform as a Service (PaaS) that enables developers to create, run, and manage applications entirely in the cloud.

To set up your Heroku account:

1.  Go to [heroku.com](https://www.heroku.com/) and sign up for a free account.
2.  During registration, specify your role as "Hobbyist" and choose Python as your primary development language.
3.  Click "Create free account."

The Gitpod Full Template from Code Institute was used for this project, which comes with the Heroku Command Line Interface (CLI) pre-installed. If you need the latest installation instructions for the Heroku CLI, refer to the [Heroku documentation](https://devcenter.heroku.com/articles/heroku-cli).

To log in to the Heroku CLI:

1.  Open your terminal and type the following command:
        
    `heroku login -i` 
    
2.  Enter your Heroku username and password when prompted.
    
If you have Multi-Factor Authentication (MFA) enabled:

1.  Visit the Heroku Dashboard and click on "Account Settings" from the avatar menu.
    
2.  Scroll down to the API Key section and click "Reveal" to see your API key. Copy it.
    
3.  Use the login command with the `-i` flag again:
        
    `heroku login -i` 
    
4.  Enter your Heroku username and paste the API key when prompted for your password.

To deploy your project on Heroku, follow these steps from the Heroku dashboard:

1.  Select "New" in the top-right corner of your Heroku Dashboard and choose "Create new app" from the dropdown menu.
2.  Provide a unique name for your app. Heroku requires a unique app name, so you may need to try different names until you find one that's available.
3.  Choose the region closest to your location (EU or USA) from the dropdown menu, and click "Create App."

In the app's "Settings" tab:

4.  Click "Reveal Config Vars" and add a new Config Var with the KEY set to `DATABASE_URL` and the value set to the ElephantSQL database URL you copied earlier.
    
5.  Add additional Config Vars for the following:
    
    -   `ALLOWED_HOST` with the URL for your deployed API (e.g., _drf-task-manager.herokuapp.com_).
    -   `CLIENT_ORIGIN` with the URL for your deployed frontend application (e.g., [https://task-manager-pp5.herokuapp.com](https://task-manager-pp5.herokuapp.com/)).
    -   `CLIENT_ORIGIN_DEV` with the URL for the development version of your frontend application (e.g., [https://3000-ujuniordev-taskmanagerp-jkhhdzrs1du.ws-us104.gitpod.io](https://3000-ujuniordev-taskmanagerp-jkhhdzrs1du.ws-us104.gitpod.io/)).
    -   `CLOUDINARY_URL` copied from your [Cloudinary](https://cloudinary.com/) dashboard if you're using Cloudinary for hosting static files.
    -   `DISABLE_COLLECTSTATIC` set to `1` since you don't need to load new static files during deployment.
    -   `SECRET_KEY` containing your secret key (also included in `env.py`).

To connect your GitHub repository to Heroku for deployment:

1.  Go to the Heroku dashboard and select "Deploy" at the top of the screen.
2.  Choose "GitHub" as the deployment method, then click "Connect to GitHub."
3.  In the "repo-name" field, search for the name of your GitHub repository and click "Search."
4.  Click "Connect" to link your GitHub repository with Heroku.
5.  Scroll down to the "Manual deploy" section and click "Deploy Branch."

Optionally, you can enable automatic deploys in the "Automatic deploys" section to have Heroku rebuild your app every time you push new changes to GitHub.

Now, push your updates to GitHub, and your project should be deployed and live on Heroku.