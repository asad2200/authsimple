# AUTHSIMPLE

authsimple is a Django app to implement simple authentication
in django project.

package link - https://pypi.org/project/django-authsimple/

Full projectSource code link - https://github.com/asad2200/BasicAuth

## Quick start

1.  Add "authentication" to your INSTALLED_APPS setting like this

        INSTALLED_APPS = [
            ...
            'authentication',
        ]

2.  Include the authentication URLconf in your project `urls.py` like this

        path('auth/', include('authentication.urls')),

3.  Create a `simpleAuth.py` file at project level(where `manage.py` is located)

        DOMAIN = "http://127.0.0.1:8000" # for default djangoserver (use your domain name)
        SENDER_EMAIL_ID = "YOUR_MAIL_ID"
        SENDER_PASSWORD = 'YOUR MAIL_ID PASSWORD'
        SERVER_NAME = 'smtp.gmail.com' # for gmail (use your mail servername)

4.  Run `python manage.py migrate` to create the authentication models.

5.  Start the development server and visit `http://127.0.0.1:8000/auth/register`
    to register user.

6.  visit `http://127.0.0.1:8000/auth/login` to login.
7.  visit `http://127.0.0.1:8000/auth/logout` to logout.
8.  visit `http://127.0.0.1:8000/auth/forgot_password` to forgot_password.
