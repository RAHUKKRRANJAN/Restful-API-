  # Restful-API#
Using Django, Django OAuth Toolkit, and OAuthLib, create an OAuth2 provider.

#What are we going to construct?#
An OAuth2 provider will be constructed from the ground up.
To get things going, we will:-

->Make a Django project?
->Set up and setup the OAuth Toolkit for Django.
->Make two apps using OAuth2.
->Apply the grant flow for authorization codes.
->Apply the grant flow for client credentials.

#What is OAuth?#
Internet users can provide websites or applications access to their information on other websites without providing them with their passwords by using the open standard OAuth for access delegation. [Wikipedia Link :- https://en.wikipedia.org/wiki/OAuth#cite_note-1]

#Django#
A high-level Python Web framework called Django promotes efficient development and simple, straightforward design. It handles a lot of the bothersome aspects of Web development and was built by seasoned developers, allowing you to concentrate on developing your app instead of having to start from scratch.[Link :- https://www.djangoproject.com/ ]

First, let's establish a virtual environment: mkproject iam
 
The new Python virtual environment will be created, activated, and its directory changed as a result.
Set up Django: pip install Django

Create a project in Django: django-admin startproject iam

In your current directory, a mysite directory will be created as a result. Using the estructure that follows:
      
      .──iam──┬──iam──┬──asgi.py
        │       ├──__init__.py
        │       ├──settings.py
        │       ├──urls.py
        │       └──wsgi.py
        └──manage.py


Create a Django application:
   
     cd iam/
     python manage.py startapp users


This will generate the directory file {users{, arranged as follows:
       
        .──iam──┬──asgi.py
        ├──__init__.py
        ├──settings.py
        ├──urls.py
        └──wsgi.py
    ├──manage.py
    └──users──┬──admin.py
           ├──apps.py
           ├──__init__.py
           ├──migrations──└──__init__.py
           ├──models.py
           ├──tests.py
           └──views.py


Even if you find that the default User model works well for you, it is strongly advised that you set up a custom user model when you begin a new project. This model functions in the same way as the default user model, but you may modify it at a later time if necessary.
User Link :- [https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User]
Django documentation Link :- [https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project]

In file {users/models.py}, add the following code:
       
        from django.contrib.auth.models import AbstractUser
        class User(AbstractUser):
         pass

In order to add a user's application to INSTALLED_APPS, edit file {iam/settings.py}.

      INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

Set up the users.By adding AUTH_USER_MODEL to file {iam/settings.py}, the user will be the model used for the auth application.
  
   AUTH_USER_MODEL='users.User'

Initial user application migration should be created. Model of user:
   
    python manage.py makemigrations

The migration will be created using the above command:

     Migrations for 'users':
     users/migrations/0001_initial.py
    - Create model User

Lastly, carry out the migration:

    python manage.py migrate

Migrate output:

              Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions, users
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0001_initial... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying users.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying sessions.0001_initial... OK


#Django OAuth Toolkit#
You may benefit from Django OAuth Toolkit's provision of all the endpoints, information, and logic required to include OAuth2 capabilities into your Django applications right out of the box.

Set up the OAuth Toolkit for Django:
    
     pip install django-oauth-toolkit

To INSTALLED_APPS, add oauth2_provider in file{iam/settings.py}
        
        INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'oauth2_provider',
]

Carry out the migration:

    python manage.py migrate

Migrate command output:
  Operations to perform:
  Apply all migrations: admin, auth, contenttypes, oauth2_provider, sessions, users
Running migrations:
  Applying oauth2_provider.0001_initial... OK
  Applying oauth2_provider.0002_auto_20190406_1805... OK

Add oauth2_provider.urls in the following manner to file{iam/urls.py}

         from django.contrib import admin
     from django.urls import include, path
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

As a result, APIs for token generation, authorization, and OAuth application creation will be made available.
Lastly, update file {iam/settings.py} with LOGIN_URL:

       LOGIN_URL='/admin/login/'

Django Admin login will be used to simplify our lives.
Establish a user:

    python manage.py createsuperuser

    Username: wiliam
    Email address: me@wiliam.dev
    Password:
    Password (again):
    Superuser created successfully.

First, we will give the following grant types a try:

Code of authorization Client credential
The majority of use cases are covered by these two grant kinds at first.

#Code of Authorization#

It is advisable to employ the Authorization Code flow in mobile and online applications. The user gives permission to your partner to access its goods through your APIs in this flow for third-party integration.

Launch the development server:

     python manage.py runserver

To build an application, point your browser to http://127.0.0.1:8000/o/applications/register/.

#Setting up MongoDB Configuration#
     In your Django project's settings.py file, configure the database settings to use MongoDB.

      DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mydatabase',  # Replace 'mydatabase' with your MongoDB database name
        'CLIENT': {
            'host': 'localhost',  # MongoDB host
            'port': 27017,  # MongoDB port
            'username': 'your_username',  # MongoDB username (if required)
            'password': 'your_password',  # MongoDB password (if required)
            'authSource': 'admin',  # MongoDB authentication database (if required)
        }
    }
}

#Creating Models#
   Define your MongoDB models in models.py inside the myproject:

# Implementing OAuth2.0 #
  ->Use Django OAuth Toolkit to handle OAuth2.0 authentication. Configure it in settings.py.
  ->Create views for registering developers and accessing protected APIs in views.py inside the myproject. Implement serializers in serializers.py.
  ->Implement serializers in serializers.py to serialize data.
  ->Configure URLs in urls.py.
  ->Finally, run your Django server:
                
      python manage.py runserver


    

 
