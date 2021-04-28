# MSP4 Lee's Burger KItchen (LBK)

![Screenshot](static/images/)

This is the Website for [Lee's Burger Kitchen(LBK)](). Which is an online burger delivery site. 

The purpose of this site is to use everything learnt from all the modules of the Full Stack Developer Course and create a Full Stack 
Django Framework project that includes the accessing, manipulating and displaying data retrieved from a relational database. 
The Website utilises a PostGres database together with Python code to access and manipulate the data. 

HTML, CSS and Javascript were used to help assist the Django frameworks with the visualization of the data. The site utilises the UI feature
called Stripe which allows online payments.

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
*  I want to be able to view total orders recieved and mark them completed.
*  I want to be able to view orders recieved and mark them completed.
 

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
* Contact Page
* Menu Page
* Product Details
* Shopping Cart
* Checkout Page
* User Profile Page
* Order History
* Admin Product Page
* Owner Order Dashboard
* Django All Auth
* Sign Up
* Login
* Forgot password
* Logout
* Back to Top
* Sorting

## Future Development
* Order Delivery tracker 
*   
 
## Database Structure


1. Profile

2. Products 

3. Category

4. Order



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
 
 [Gunicorn]():

 [Psycopg2]():
 
 [Stripe]():
 
 [Django Crispy Forms]():

**Tools**

[Git](https://git-scm.com/): 
 Git was used by utilizing the Gitpod terminal to commit to Git and push to GitHub.

[GitHub](https://github.com/):
 GitHub was used to create a repository and store the code after it was pushed from Git.

[Pip]():

[Heroku](https://www.heroku.com):
 Heroku was used to deploy my app.

[AWS S3 Bucket]():

[Balsamiq](https://balsamiq.com/):
 Wireframes were created using Balsamiq

[Pixabay](https://pixabay.com/):
 Pixabay was used to source the background imagery for the webpage.


**Databases**

[SQlite3]():

[PostgresSQL]():

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
### 1.  

## Testing User Stories

**External User Goals:**
    
* 

    (a)  

    (b)  
    ![]()



### Site Owner's Goals:
* 

    (a) 

    (b) 

    
## Bugs
- 

# Deployment 

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
                 
    - IP                  
    - PORT               
    - SECRET_KEY          
    - MONGO_URI
    - MONGO_DBNAME
  

7. In the "Manual Deployment" section of this page, make sure the master branch is selected and then click "Deploy Branch".

8. The site is now successfully deployed, click the "Open app" button to visit it.



# Credits

**Code**
* 

**Content & Media**




**Acknowledgements**

* My Mentor Aaron Sinnott for feedback
* Code Institute for training
* WS3 schools for reference on coding issues
* Stackoverflow for reference on coding issues
* YouTube online tutorials used when encountered coding issues