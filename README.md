# MSP4 Lee's Burger KItchen (LBK)

![Screenshot](static/images/)

This is the Website for [Lee's Burger Kitchen(LBK)](). Which is an online burger delivery site. 

The purpose of this site is to use everything learnt from all the modules of the Full Stack Developer Course and create a Full Stack 
Django Framework project that includes the accessing, manipulating and displaying data retrieved from a relational database. 
The Website utilises a PostGres database together with Python code to access and manipulate the data. 

HTML, CSS and Javascript were used to help assist the Django frameworks with the visualization of the data. The site utilises the UI feature called Stripe which allows online payments.

------

# User Experience (UX)

## User stories
### Common user stories (guests, new users and authenticated users)

As a User....
*  I expect to access the website from any device, so that I can use the website anytime and anywhere.
*  I expect to easily navigate the website, so that I can quickly find what I'm looking for.
*  I want to find an information about the company, to know what they do, what their main principles and ideas
*  I want to see the location of the LBK.
*  I want to be able to easily contact the owner/manager of the company, so that I can write an additional query or ask a question.
*  I want to view all available products.
*  I want to view product details (e.g. image, price, description, ingredients), so that I can make an informed decision before I buy.
*  I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
*  I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment.
*  I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
*  I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.
*  I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.
*  I want to receive an email confirmation that my product is on the way.


### New Users
As a new user....
* I want to create my own account, so that I can save, view and edit my profile details and view my order history.

### Returning users
As a returning user....
*  I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.
*  I want to reset my password if I forgot it, so that I can get access to my profile again.
*  I want to be able to change my password, so that I can create the stronger password (e.g.in case I published my old password somewhere) to protect my personal details.
*  I want to be able to change my email or add the second email, so that I can have an easier access to the website's functionality and to gain more flexibility.
 
### Website Owner(admin)
As a Site owner....
*  I want to secure admin interface avalable only for website admin, so that I can add, edit and remove products.
*  I want to be able to view orders recieved  for that day and update the order status.
*  I want to be able to differentiate between active orders and completed orders for the day.
*  I want to be able to view history of all orders recieved.   

## Design

### Frameworks

- Bootstrap, front-end framework was chosen for this project for its ease of use and ability to be easily customized. 
It was used for creating features such as navbar, cards, forms, modals, as well as for the layout.
- JQuery is used for initializing some Bootstrap components.

### Colour Scheme

The main goals of UI is to focus the user's attention on the product images therefore simple greys, whites and blacks where used to create
a clean and neat background. 


### Typography 
    
The Font Barlow Condensed was used from google fonts accross the site as its a clean and simple font.

### Icons
        
Icons from fontawesome where used throughout the site as the grab the users attention. They create a more user-friendly experience for 
users as they give visual clues about the subject. Icons used across the project for social media links, forms, cart, search bar and the 
navigation are similar to what the user would see in other sites giving them a sense of familiarity.

### Imagery  

The main image has been chosen to be eye catching and gives the user a clear indication of what the website is about.
The other images have been choosen to highlight the product in an appealing light.  
    
    
## Wireframes:
The [LBK](docs/LBK.pdf) wireframes can be found here.
 
------

# Features

## Existing Features

* Navbar
* Footer
* Home page
* About Page
* Menu Page
* Product Details
* Shopping Cart
* Checkout Page
* User Profile Page
* Update Profile details
* User Order History
* Admin Product Page
* Owner Order Dashboard
* Owner Order Details/Status Update
* Create your own burger page.
* Django All Auth
* Sign Up
* Login
* Forgot password
* Logout
* Back to Top
* User Reviews
* Add review

## Future Development
* Order Delivery tracker 
* Apple & Google Pay
* Social Account Login feature 

 
## Database Structure


1. Profile
- User Profiles

2. Products 
- Categorys
- Custom_burgers
- Ingredients
- Products

3. Customers
- Reviews

4. Checkout
- Orders


# Technologies Used
 
 **Languages** 
- HTML
- CSS
- Python
- Javascript
- Jinja
 

**Libraries & Frameworks**
   
[Django]():

[Bootstrap]():
 
[Font Awesome](https://fontawesome.com/):
 Font Awesome was used to provide the Icons throughout this website.

[Google Fonts](https://fonts.google.com/):
 Google fonts was used to import the font into the style.css file

[JQuery](https://jquery.com/):
 JQuery was used to run the scripts for the following:

[Pillow]():
 
[Gunicorn](https://gunicorn.org/):
 Was installed and used as the webserver

[Psycopg2](https://pypi.org/project/psycopg2/):
 Psycopg2 was utilised as the PostgreSQL database adapter for the project.
 
[Stripe](https://stripe.com/gb):
 Stripe was used for the online payment processing when customer uses the checkout.
 
[Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/):
 Django Crispy Forms was used to render the behavior of the forms in this project.

[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html):
 Boto3 was used along with AWS to create, configure, and manage AWS services.

[Django Storages](https://django-storages.readthedocs.io/en/latest/):
 Django Storages was used as the backend storages for connecting with S3

**Tools**

[Git](https://git-scm.com/): 
 Git was used by utilizing the Gitpod terminal to commit to Git and push to GitHub.

[GitHub](https://github.com/):
 GitHub was used to create a repository and store the code after it was pushed from Git.

[Pip](https://pip.pypa.io/en/stable/installing/):
 Pip was used to istall python packages/modules required for the project.

[Heroku](https://www.heroku.com):
 Heroku was used to deploy my app.

[AWS S3 Bucket](https://aws.amazon.com/):
 AWS S3 was used to store the static files and the images for the project.

[Balsamiq](https://balsamiq.com/):
 Wireframes were created using Balsamiq

[Pixabay](https://pixabay.com/):
 Pixabay was used to source the background imagery for the webpage and Burger Images.

[Istock](https://www.istockphoto.com/): 
 Istock was used to source the background imagery for the webpage and Burger Images.

[Pexels](https://www.pexels.com/):
 Pexels was used to source the background imagery for the webpage and Burger Images.

[Imgur](https://imgur.com/): 
 Was used to upload my images and create a url for the database upload.


**Databases**

[SQlite3](https://sqlite.org/index.html):
 SQLite3 was used as the developmental database before deploying to Heroku.

[PostgresSQL](https://www.postgresql.org/):
 Postgres SQL was used as the relational database after to deploying to Heroku.

# Testing
### Code Validation
The Freeformatter HTML Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no errors in the project.

[CSS Validator](http://jigsaw.w3.org/css-validator/) - [Results]()

[HTML Validator](https://validator.w3.org/) - [Results](docs/) the results show a warning "lack of heading for section", the section displays 
the flash messages that displays success/error messages when user logs in, adds/removes files.

[JSHint](https://jshint.com/) - [Results](docs/)

Lighthouse was used on Google Chrome to help improve perfomance and accessability. This helped improve the contrast issue with background
and foreground colours - [Results](docs/)


### Devices
The website was tested on laptop, desktop, iphone, ipad on the following browsers:
- Google Chrome
- Microsoft Edge
- Safari
- Firefox 

### Manual Tests for functionality of features
### 1. Navbar
-
-
### 2. Footer
-
-
### 3. Home page
-
-
### 4. About Page
-
-
### 5. Menu Page
-
-
### 6. Product Details
-
-
### 7. Shopping Cart
-
-
### 8. Checkout Page
-
-
### 9. User Profile Page
-
-
### 10. Update Profile details
-
-
### 11. User Order History
-
-
### 12. Admin Product Page
-
-
### 13. Owner Order Dashboard
-
-
### 14. Owner Order Details/Status Update
-
-
### 15. Create your own burger page.
-
-
### 16. Django All Auth
-
-
### 17. Sign Up
-
-
### 18. Login
-
-
### 19. Forgot password
-
-
### 20. Logout
-
-
### 21. Back to Top
-
-
### 22. User Reviews
-
-

## 23. Add review
-
-

## Testing User Stories

**External User Goals:**

As a User....
*  I expect to access the website from any device, so that I can use the website anytime and anywhere.
    (a)  

    (b)  
    ![]()
*  I expect to easily navigate the website, so that I can quickly find what I'm looking for.
*  I want to find an information about the company, to know what they do, what their main principles and ideas
*  I want to see the location of the LBK.
*  I want to be able to easily contact the owner/manager of the company, so that I can write an additional query or ask a question.
*  I want to view all available products.
*  I want to view product details (e.g. image, price, description, ingredients), so that I can make an informed decision before I buy.
*  I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
*  I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment.
*  I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
*  I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.
*  I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.
*  I want to receive an email confirmation that my product is on the way.


### New Users
As a new user....
* I want to create my own account, so that I can save, view and edit my profile details and view my order history.

### Returning users
As a returning user....
*  I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.
*  I want to reset my password if I forgot it, so that I can get access to my profile again.
*  I want to be able to change my password, so that I can create the stronger password (e.g.in case I published my old password somewhere) to protect my personal details.
*  I want to be able to change my email or add the second email, so that I can have an easier access to the website's functionality and to gain more flexibility.
 
### Website Owner(admin)
As a Site owner....
*  I want to secure admin interface avalable only for website admin, so that I can add, edit and remove products.
*  I want to be able to view orders recieved  for that day and update the order status.
*  I want to be able to differentiate between active orders and completed orders for the day.
*  I want to be able to view history of all orders recieved.   
 

    
## Bugs
- After deploying to Heroku Menu image links were broken as the file url wasn't included in the media folder upload. These were added in the admin section.

- After deploying a Server Error 500 message appeared after confirming payment in the checkout app. Debug was turned back on to True to discover where the issue was ![error](static/images/error.png). This error was due to the order_id in the models.py having a max-length of 28 when the UUID is 32 characters. This issue was corrected and migrations where ran but the error still occured. After contacting Tutor support it was highlighted that there were existing orders in the developembntal database that was causing this error. These orders were deleted from the admin section, the postgress database was reset and the data was dumped into jason.db and reimported.

- After creating the Custom_burger cfreator an integrity Error occured on the Heroku app when clicking the create burger button. This error was resolved by adding a price field in the Custom_burger model and giving it a default value.


# Deployment 

Lees Burger Kitchen was developed using [GitPod](https://www.gitpod.io/) using Git & GitHub for version control. 
It is hosted on the [Heroku](https://heroku.com/) platform, with static files hosted in AWS S3 Basket.

### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE of your choice (I used [GitPod](https://www.gitpod.io/) for creating this project)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python3](https://www.python.org/)    

Accounts will need to be created for the following services:
- [Stripe](https://stripe.com/en-ie)
- [AWS](https://aws.amazon.com/) to setup the [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- An Email account for this project I used [Gmail](https://mail.google.com/)

#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/Leeap83/Lee-s_Burger_Kitchen.git`          

More information about the cloning process can be found here: [GitHub Help page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).   

2. Set up environment variables.     
Note, that this process will be different depending on IDE you use.   
In this it was done using the following way:      
    - Create `.env` file in the root directory.
    - Add `.env` to the `.gitignore` file in your project's root directory
    - In `.env` file set environment variables with the following syntax:     
    ```bash 
    import os  
    os.environ["DEVELOPMENT"] = "True"    
    os.environ["SECRET_KEY"] = "<Your Secret key>"    
    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
    os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
    os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"    
     ```
    
3. Install all requirements from the **requirements.txt** file putting this command into your terminal:     
`pip3 install -r requirements.txt`     
4. In the terminal in your IDE migrate the models to crete a database using the following commands:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`     
5. Load the data fixtures(**categories**, **products**) in that order into the database using the following command:    
`python3 manage.py loaddata <fixture_name>`        
6. Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):    
`python3 manage.py createsuperuser`   
7. You will now be able to run the application using the following command:     
`python3 manage.py runserver`     
8. To access the admin panel, you can add the `/admin` path at the end of the url link and login using your superuser credentials.

### Heroku Deployment
The project was deployed to [Heroku](https://dashboard.heroku.com/apps) Pages using the following steps...

To deploy the project on heroku, take the following steps:

1. If not already present, create a requirements.txt file using the command:

    pip freeze > requirements.txt

2. If not already present, create a `Procfile` with the command:

    echo web: python app.py > Procfile

3. Push the the project to GitHub.

4. Log in to your Heroku account and create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the 
"New" button in your dashboard. Give it a name and set the region to the one closest to you, then click the "Create app" button.

5.  Click on "Deploy" tab and under "Deployment method" and select GitHub. Select the correct repository and click "Connect".

6. Click on the "Settings" tab and under "Config Vars" click "Reveal Config Vars" and enter the Key and values stored in
the env.py file:
                 
| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_HOST_PASS | `<your email password(generated by Gmail)>` |
| EMAIL_HOST_USER| `<your email address>`  |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
| STRIPE_SECRET_KEY| `<your stripe secret key>`  |
| STRIPE_WH_SECRET| `<your stripe wh key>`  |
| USE_AWS | `True`  |
  

7. In the "Manual Deployment" section of this page, make sure the master branch is selected and then click "Deploy Branch".

8. The site is now successfully deployed, click the "Open app" button to visit it.



# Credits

**Code**
* [Code Institute](https://codeinstitute.net/) The project's code was developed by following the video lessons for the Boutique Ado Django Mini-Project, but was customized, modified and enhanced to fit the project purposes. 
* Animation on the homepage was implemented following JulioCodes [Youtube](https://www.youtube.com/c/JulioCodes)
* Kevin Loughrey & Scott Kipp from tutor support for help with my "Server Error 500" error.

**Content & Media**

Burger Images and homepage images were downloaded from Pexels from the following Users:
* https://www.pexels.com/@taryn-elliott
* https://www.pexels.com/@valeriya
* https://www.pexels.com/@atomlaborblog
* https://www.pexels.com/@jonathanborba
* https://www.pexels.com/@seyed-ali-hosseini-1226419
* https://www.pexels.com/@geraud-pfeiffer

Istock Credits were purchased and images were downloaded from the following:
* https://www.istockphoto.com/portfolio/vaaseenaa?mediatype=photography
* https://www.istockphoto.com/portfolio/comicsans?mediatype=illustration
* https://www.istockphoto.com/portfolio/Fudio?mediatype=photography
* https://www.istockphoto.com/portfolio/bhofack2?mediatype=photography


**Acknowledgements**

* My Mentor Aaron Sinnott for feedback
* Code Institute for training
* Tutor Suport for assistance with code errors
* Slack for reference on coding issues
* WS3 schools for reference on coding issues
* Stackoverflow for reference on coding issues
* YouTube online tutorials used when encountered coding issues